"""Compare a rule template with recorded real model outputs, without new API calls.

This measures contract/action agreement only, not human editing time or quality.
"""
import importlib.util
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("prototype", ROOT / "starter-code/prompt_prototype.py")
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


def main():
    source = ROOT / "evidence/live-results.json"
    recorded = json.loads(source.read_text(encoding="utf-8"))
    rows = []
    for item in recorded["results"]:
        if "raw_output" not in item:
            continue
        context = item["trusted_context"]
        start = time.perf_counter()
        baseline_raw = lab.build_rule_template(context)
        elapsed_ms = round((time.perf_counter() - start) * 1000, 4)
        baseline = lab.validate_response(baseline_raw, context)
        try:
            model = lab.validate_response(item["raw_output"], context)
            model_pass = True
        except lab.BoundaryViolation:
            model, model_pass = {}, False
        rows.append({
            "name": item["name"], "trusted_context": context,
            "rule_template_output": baseline_raw,
            "recorded_model_output": item["raw_output"],
            "rule_contract_pass": True, "model_contract_pass_current_validator": model_pass,
            "action_agreement": model.get("action") == baseline["action"],
            "rule_generation_ms_single_observation": elapsed_ms,
            "rule_draft_words": len(baseline["draft_message"].split()),
            "model_draft_words": len(model.get("draft_message", "").split()),
            "human_edit_seconds": None, "human_quality_score": None,
        })
    result = {
        "mode": "offline_comparison_with_recorded_live_outputs",
        "new_api_calls": 0, "source_evidence": source.relative_to(ROOT).as_posix(),
        "source_executed_at_utc": recorded["executed_at_utc"],
        "source_model": recorded["model"], "source_prompt_version": recorded["prompt_version"],
        "validator_version": lab.VALIDATOR_VERSION, "paired_cases": len(rows),
        "rule_contract_passes": sum(x["rule_contract_pass"] for x in rows),
        "model_contract_passes": sum(x["model_contract_pass_current_validator"] for x in rows),
        "action_agreements": sum(x["action_agreement"] for x in rows),
        "human_review": "not_performed", "results": rows,
        "conclusion": "The template meets checked contracts on this small paired sample. "
                      "No measured LLM superiority in human quality, editing time or ROI is claimed.",
    }
    (ROOT / "evidence/template-comparison.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Đối chứng Rule + template và output LLM đã ghi nhận", "",
             "Đây là đối chứng offline trên cùng context của output model thật đã lưu; không gọi API mới.",
             "Không dùng fixture tự tạo làm kết quả model, không có reviewer người dùng hoặc thời gian sửa thực đo.", "",
             f"Nguồn: `{result['source_evidence']}`, model `{result['source_model']}`, "
             f"prompt `{result['source_prompt_version']}`; chấm lại bằng validator `{lab.VALIDATOR_VERSION}`.", "",
             "| Case | Template contract | LLM contract | Action giống nhau | Số từ nháp template / LLM |",
             "|---|---|---|---|---|",]
    for row in rows:
        lines.append(f"| {row['name']} | PASS | {'PASS' if row['model_contract_pass_current_validator'] else 'FAIL'} "
                     f"| {'Có' if row['action_agreement'] else 'Không'} "
                     f"| {row['rule_draft_words']} / {row['model_draft_words']} |")
    lines += ["", f"**Mẫu ghép cặp: {len(rows)} case.** Template đạt "
              f"{result['rule_contract_passes']}/{len(rows)}; LLM đạt {result['model_contract_passes']}/{len(rows)} "
              f"theo validator hiện tại; action trùng {result['action_agreements']}/{len(rows)}.", "",
              "## Diễn giải", "",
              "Rule + template đã giải được quyết định có cấu trúc trong mẫu này. Chênh lệch số từ chỉ mô tả độ dài, "
              "không phải điểm chất lượng. Chưa có dữ liệu chứng minh LLM giúp người duyệt sửa ít hơn hoặc nhanh hơn. "
              "Baseline template vì vậy là lựa chọn triển khai đầu tiên nếu discovery xác nhận pain; LLM vẫn là thử nghiệm.", "",
              "Để quyết định dùng LLM, cần reviewer đánh giá mù trên cùng case và rubric đã chốt; đo thời gian sửa thật. "
              "Thời gian sinh template trong JSON chỉ là một quan sát local, không so với API latency để kết luận hiệu suất nghiệp vụ.", "",
              "Không suy rộng mẫu development này thành held-out benchmark, độ chính xác toàn hệ thống hay ROI thực tế.", ""]
    (ROOT / "evidence/template-comparison.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["paired_cases", "rule_contract_passes", "model_contract_passes", "action_agreements", "new_api_calls"]}))


if __name__ == "__main__":
    main()
