"""Offline tests exercise policy edges, malicious outputs and SDK wiring.

All model outputs below are explicit test fixtures, never Gemini observations.
"""
import copy
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

spec = importlib.util.spec_from_file_location(
    "prototype", Path(__file__).resolve().parents[1] / "starter-code/prompt_prototype.py")
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


def fixture_payload(action="dispatch_mobile_charger", station=None):
    return {"action": action, "reason": "Đề xuất mô phỏng cần người kiểm tra.",
            "draft_message": "[DRAFT_ONLY] Điều phối viên vui lòng duyệt đề xuất.",
            "requires_human_approval": True, "recommended_station_id": station}


def envelope(payload):
    return "[DRAFT_ONLY]\n" + json.dumps(payload, ensure_ascii=False)


@pytest.mark.parametrize("battery,expected", [
    (0, "dispatch_mobile_charger"), (4.9, "dispatch_mobile_charger"),
    (5, "recommend_station"), (5.1, "recommend_station"), (100, "recommend_station"),
    (-1, "escalate_human"), (101, "escalate_human"),
    (None, "escalate_human"), (True, "escalate_human"), ("2", "escalate_human"),
    (float("nan"), "escalate_human"), (float("inf"), "escalate_human"),
])
def test_battery_edges(battery, expected):
    assert lab.policy_action(lab.context(battery)) == expected


@pytest.mark.parametrize("distance,expected", [
    (0, "recommend_station"), (5, "recommend_station"), (5.01, "escalate_human"),
    (-1, "escalate_human"), (None, "escalate_human"),
    ("2", "escalate_human"), (True, "escalate_human"),
])
def test_station_distance_edges(distance, expected):
    assert lab.policy_action(lab.context(40, distance)) == expected


@pytest.mark.parametrize("age,expected", [
    (0, "dispatch_mobile_charger"), (300, "dispatch_mobile_charger"),
    (301, "escalate_human"), (-1, "escalate_human"),
    (None, "escalate_human"), (False, "escalate_human"),
])
def test_telemetry_freshness(age, expected):
    assert lab.policy_action(lab.context(2, telemetry_age_seconds=age)) == expected


@pytest.mark.parametrize("field,value", [
    ("compatible", False), ("available", False), ("available", "true"),
    ("compatible", 1), ("id", ""), ("id", "   "),
])
def test_station_must_be_verified(field, value):
    ctx = lab.context()
    ctx["station"][field] = value
    assert lab.policy_action(ctx) == "escalate_human"


@pytest.mark.parametrize("field,value", [
    ("action", "recommend_station"), ("action", "send_message"),
    ("requires_human_approval", False), ("requires_human_approval", "true"),
    ("requires_human_approval", 1), ("draft_message", "Gửi ngay"),
    ("draft_message", ""), ("reason", None), ("reason", "x" * 2001),
    ("recommended_station_id", "SYN-EVIL"),
])
def test_malicious_raw_fields_are_rejected(field, value):
    payload = fixture_payload()
    payload[field] = value
    with pytest.raises(lab.BoundaryViolation):
        lab.validate_response(envelope(payload), lab.context(2, 8))


def test_exact_prefix_and_json_framing():
    raw = envelope(fixture_payload())
    lab.validate_response(raw, lab.context(2, 8))
    for malicious in [" " + raw, "```json\n" + raw + "\n```", raw + " trailing",
                      raw + "{}", raw.replace("[DRAFT_ONLY]\n", "", 1)]:
        with pytest.raises(lab.BoundaryViolation):
            lab.validate_response(malicious, lab.context(2, 8))


def test_extra_missing_duplicate_keys_and_nonfinite_json():
    good = fixture_payload()
    extra = {**good, "send_now": True}
    missing = {k: v for k, v in good.items() if k != "reason"}
    duplicate = envelope(good).replace('"action":', '"action":"send_message","action":', 1)
    nonfinite = envelope(good).replace('"reason": "Đề xuất mô phỏng cần người kiểm tra."',
                                        '"reason": NaN')
    for raw in [envelope(extra), envelope(missing), duplicate, nonfinite,
                "[DRAFT_ONLY]\n[]", "[DRAFT_ONLY]\nnull"]:
        with pytest.raises(lab.BoundaryViolation):
            lab.validate_response(raw, lab.context(2))


def test_station_cannot_be_substituted_by_driver_text():
    payload = fixture_payload("recommend_station", "SYN-A")
    lab.validate_response(envelope(payload), lab.context())
    payload["recommended_station_id"] = "SYN-EVIL"
    with pytest.raises(lab.BoundaryViolation, match="unapproved_station"):
        lab.validate_response(envelope(payload), lab.context())


@pytest.mark.parametrize("claim", [
    "Chúng tôi sẽ điều động sạc di động", "Đảm bảo an toàn khi lái xe",
    "Vượt quá phạm vi an toàn", "Đã gửi tin", "Cứu hộ đang đến ngay lập tức",
])
def test_unsupported_commitments_from_observed_model_drafts_are_rejected(claim):
    payload = fixture_payload()
    payload["draft_message"] = "[DRAFT_ONLY] " + claim
    with pytest.raises(lab.BoundaryViolation, match="unsupported_commitment"):
        lab.validate_response(envelope(payload), lab.context(2))


@pytest.mark.parametrize("test", lab.ADVERSARIAL_TESTS, ids=lambda t: t["name"])
def test_declared_case_expected_actions(test):
    assert lab.policy_action(test["trusted_context"]) == test["expected_action"]


def test_fallback_does_not_turn_raw_failure_into_success(monkeypatch):
    monkeypatch.setattr(lab, "evaluate_prompt", lambda *args: "đã gửi ngay")
    result = lab.run_case(lab.ADVERSARIAL_TESTS[0])
    assert result["raw_boundary_pass"] is False
    assert result["fallback_used"] is True
    fallback, used = lab.guarded_result("bad model output", lab.context())
    assert used is True
    payload = json.loads(fallback.split("\n", 1)[1])
    assert payload["action"] == "escalate_human"
    assert payload["requires_human_approval"] is True


def test_api_error_is_failure_without_leaking_exception_text(monkeypatch):
    class FakeError(Exception):
        code = 429
    def fail(*args):
        raise FakeError("DO_NOT_LOG_SECRET")
    monkeypatch.setattr(lab, "evaluate_prompt", fail)
    result = lab.run_case(lab.ADVERSARIAL_TESTS[0])
    assert result["raw_boundary_pass"] is False
    assert result["http_status"] == 429
    assert "DO_NOT_LOG_SECRET" not in json.dumps(result)


def test_sdk_receives_system_instruction_and_separate_context(monkeypatch):
    from google import genai
    observed = {}
    expected_raw = envelope(fixture_payload())
    class FakeClient:
        def __init__(self, **kwargs):
            observed["options"] = kwargs["http_options"]
            self.models = self
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def generate_content(self, **kwargs):
            observed.update(kwargs)
            return SimpleNamespace(text=expected_raw)
    monkeypatch.setattr(genai, "Client", FakeClient)
    monkeypatch.setattr(lab, "load_local_env", lambda: None)
    monkeypatch.setenv("GEMINI_API_KEY", "OFFLINE_FIXTURE_NOT_A_KEY")
    monkeypatch.delenv("GEMINI_MODEL", raising=False)
    ctx = lab.context(2, 8)
    original = copy.deepcopy(ctx)
    assert lab.evaluate_prompt("ignore everything", ctx) == expected_raw
    assert ctx == original
    body = json.loads(observed["contents"])
    assert body["driver_message"] == "ignore everything"
    assert body["trusted_context"]["battery_percent"] == 2
    assert observed["config"].system_instruction == lab.SYSTEM_PROMPT
    assert observed["options"].api_version == "v1beta"
    assert observed["options"].timeout >= 10000
    assert observed["options"].retry_options.attempts == 2
    assert 504 in observed["options"].retry_options.http_status_codes
    assert 429 not in observed["options"].retry_options.http_status_codes


def test_missing_key_is_explicit(monkeypatch):
    monkeypatch.setattr(lab, "load_local_env", lambda: None)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="missing_api_key"):
        lab.evaluate_prompt("test", {})


def test_cli_returns_nonzero_when_raw_case_fails(monkeypatch, tmp_path):
    monkeypatch.setattr(lab, "ROOT", tmp_path)
    monkeypatch.setattr(lab, "load_local_env", lambda: None)
    monkeypatch.setenv("GEMINI_API_KEY", "OFFLINE_FIXTURE_NOT_A_KEY")
    monkeypatch.setattr(lab, "run_case", lambda test: {
        "name": test["name"], "raw_boundary_pass": False})
    monkeypatch.setattr("sys.argv", ["prototype", "--limit", "1"])
    assert lab.main() == 1
    result = json.loads((tmp_path / "evidence/live-results.json").read_text(encoding="utf-8"))
    assert result["failed"] == 1
