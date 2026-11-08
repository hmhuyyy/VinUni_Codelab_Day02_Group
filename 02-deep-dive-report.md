# Phase 3 & 5 — Deep-Dive Report and Evaluation

> **Scope:** Individual draft for group review. This report scopes an Xanh SM electric-fleet low-battery assistance workflow to match the prompt prototype. The workflow and operational figures below are hypotheses, not confirmed Xanh SM internal process data. Validate them with operators and telemetry before implementation.

## Selected problem

When an electric vehicle reports battery below 5%, the operator needs to verify the vehicle's battery level and location, then prepare a safe assistance plan. The prototype must not recommend a charging station more than 5 km away and must never claim that a mobile charger has actually been dispatched.

## 3.1 Current-State Workflow Mapping

### Current-state hypothesis

1. 🔄 The vehicle telemetry or driver reports a low-battery alert to the operations team.
2. 🔄 The driver shares the current vehicle location and battery reading; an operator checks that the information is current.
3. 🔴 The operator identifies available options and checks whether a charging station is within a safe distance. For a battery level below 5%, a station over 5 km away must not be recommended.
4. The operator contacts the appropriate assistance resource, such as a mobile charging team, and waits for availability confirmation.
5. 🔄 The operator reviews and communicates the approved plan to the driver.
6. The driver acknowledges the plan and proceeds only when instructed by an authorized human.

### Handoffs and bottleneck

- **Handoffs:** vehicle/driver → operations; operations → assistance resource; operations → driver.
- **Potential bottleneck:** manually verifying telemetry/location and coordinating assistance availability.
- **Time per case:** baseline is unknown. Measure alert-to-verified-plan time and time spent by each role; do not treat an estimate as an observed result.
- **Workflow diagram:** [04-workflow-diagram.pdf](./04-workflow-diagram.pdf).

### Baseline data to collect

For a representative sample of low-battery incidents, record alert time, verified battery/location, operator handling time, assistance availability/arrival, chosen resolution, and whether the driver needed to contact operations again. Exclude personal identifiers from the prototype dataset.

## 3.2 Problem Statement (6-field) & Metrics

| Field | Details |
|---|---|
| **1. Actor / Operator** | Xanh SM driver and fleet operations controller; a mobile charging operator may be involved. Roles and handoffs need confirmation with the operations team. |
| **2. Current Workflow** | A low-battery alert or driver report is received → an operator verifies battery and location → checks safe charging/assistance options → contacts the appropriate resource → reviews and communicates the plan to the driver. This is a workflow hypothesis; the actual systems and steps are not yet verified. |
| **3. Bottleneck** | Verification of current telemetry/location and manual coordination of assistance. The time and incident frequency have not yet been measured. |
| **4. Business Impact** | Delayed assistance may increase vehicle downtime, driver workload, passenger disruption, and risk from an unsuitable route. Financial or SLA impact is unknown until incident logs and operator interviews establish a baseline. |
| **5. Success Metric** | **Safety gate:** 100% of validated cases with battery below 5% produce no recommendation for a station over 5 km away. **Prototype quality:** all required response fields present and all responses begin with `[DRAFT_ONLY]` on the acceptance set. **Operational target to validate:** reduce alert-to-human-approved-plan time to under 2 minutes without increasing incorrect or unnecessary dispatch recommendations. Establish baseline before claiming improvement. |
| **6. Operational Boundary** | The model may draft a structured recommendation from verified inputs. It must not infer missing battery/location values, recommend a station over 5 km away when battery is below 5%, execute a dispatch, change a route, cancel a ride, set a price, or send a customer message. A human operator must verify inputs and approve any action. If data is missing, confidence is low, or the service is unavailable, stop and use the existing manual escalation process. |

## 3.3 Future-State Flow & AI Fit

### AI-Fit assessment

| Option | Fit | Reason |
|---|---|---|
| **Rule / State-Machine** | **Primary** | The battery threshold and 5 km limit are explicit safety rules. They should be enforced deterministically, not entrusted to an LLM. |
| **LLM Feature** | **Limited supporting role** | It can format a human-readable explanation or draft from verified, structured inputs. It cannot determine whether a real dispatch is available or execute it. |
| **Agentic Loop** | **Not appropriate for this prototype** | Autonomous tool use or dispatch would cross the operational boundary and add risk without evidence of need. |

### Future-state flow

1. Receive a low-battery alert and retrieve the associated telemetry.
2. **Rule check:** verify battery and location are present, current, and within configured limits. If not, stop and ask an operator to verify.
3. **Rule check:** if battery is below 5%, prohibit recommendations to stations farther than 5 km and select the mobile-assistance option as a *proposal*.
4. 🔵 **AI step:** generate a short `[DRAFT_ONLY]` explanation and structured proposal using only the verified input fields.
5. 🟢 **Human step (HITL):** the operator checks the telemetry, resource availability, and proposal, then approves or edits it.
6. An authorized operator—not the model—contacts the assistance resource and communicates the approved plan.
7. ↩️ **Fallback:** on missing/stale data, invalid output, model/API failure, or uncertainty, show no recommendation and return to the existing manual escalation process.

### Prototype evidence and limitations (Phase 4)

- The two adversarial tests run so far passed: the 2% battery case produced a mobile-charger proposal without recommending the 8 km station, and the send-directly request retained `[DRAFT_ONLY]`.
- These are prompt-level checks on two examples, not proof of production safety or model reliability.
- A third test for missing telemetry and prompt injection has been added to the prototype but still needs to be run with a valid API key.
- The prototype has no live dispatch integration; an `action` in its output is a proposal only.

## Phase 5 — Evaluate

### AI Readiness Checklist

- [ ] Clean, representative operational logs and a labeled test set are available. **Not confirmed.**
- [ ] Risk is controlled by tested deterministic guardrails, human approval, monitoring, and fallback. **Designed, but not yet validated end-to-end.**
- [ ] Operations stakeholders have reviewed the workflow and are ready to adopt it. **Not confirmed.**

### Decision: **NOT YET**

The prompt prototype is a useful scoping experiment: the two executed adversarial cases passed, and the proposed scope includes human review and a manual fallback. That is not enough evidence to begin operational deployment. First confirm the current workflow with Xanh SM operators, obtain privacy-reviewed and representative incident data, measure baseline handling time, run the expanded test set (including the new missing-telemetry case), and enforce the battery/distance rules outside the LLM. Reassess after those checks; a narrow offline pilot may then be considered.
