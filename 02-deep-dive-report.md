# 02 — Deep-Dive Report: Xanh SM Vehicle Incident Report Triage

## Phase 3 — DEEP-DIVE

### 3.1 Current-State Workflow

**Selected problem:** Manual classification and routing of vehicle incident reports submitted by Xanh SM drivers.

The following workflow is a proposed baseline for analysis. Processing times are assumptions that should be validated with actual operational data.

| Step | Actor | Activity | Estimated Time |
|---|---|---|---:|
| 1 | Driver | Notices a vehicle incident and submits a report through the app or contacts the dispatcher. | 2 min |
| 2 | Dispatcher | Receives and reads the incident report. | 2 min |
| 3 | Dispatcher | Contacts the driver to clarify missing or unclear information. | 3 min |
| 4 | Dispatcher | Identifies the incident type and determines its priority. | 2 min |
| 5 | Dispatcher | Routes the report to the appropriate technical or support department. | 1 min |
| | | **Total estimated processing time** | **10 min** |

**Main bottleneck:** Incident reports are often unstructured or incomplete. Dispatchers must manually interpret the information, contact drivers for clarification and determine the appropriate department. This increases handling time and may delay incident response.

**Operational handoffs:**
- Driver → Dispatcher: Incident report submission.
- Dispatcher → Driver: Request for clarification.
- Dispatcher → Technical/Support team: Incident routing.

### 3.2 Problem Statement — Six Fields

| Field | Description |
|---|---|
| Actor | Drivers, dispatchers and technical/support teams. |
| Current workflow | Drivers submit incident reports. Dispatchers read, clarify, classify and route the reports manually. |
| Bottleneck | Unstructured information and missing details require repeated communication and manual classification. |
| Business impact | Increased dispatcher workload, longer handling time and potential delays in responding to vehicle incidents. |
| Success metrics | Reduce average handling time from an estimated 10 minutes to less than 2 minutes; achieve at least 90% classification accuracy; escalate all dangerous or unclear cases to a human dispatcher. |
| Operational boundary | AI may extract information, classify incidents and suggest priority and department. It must not autonomously dispatch emergency assistance or determine whether a vehicle is safe to operate. A human dispatcher must approve routing. |

### 3.3 Future-State Workflow

The proposed AI-assisted workflow is:

1. Driver submits a vehicle incident report.
2. LLM analyzes the natural-language report and extracts relevant information:
   - Vehicle information.
   - Incident location.
   - Incident time.
   - Symptoms and incident description.
3. LLM suggests an incident category and responsible department.
4. Rule-based logic checks predefined priority and escalation conditions.
5. Dispatcher reviews the extracted information and AI recommendation.
6. Dispatcher approves or corrects the classification and confirms routing.
7. If the report is incomplete, unclear or potentially dangerous, it is escalated to a human for immediate review.

**Fallback mechanism:**

If the AI service or API is unavailable, the system returns to the existing manual reporting and classification process. The workflow must not block incident handling because of AI failure.

### 3.4 AI Fit Assessment

| Approach | Suitability | Role in the proposed solution |
|---|---|---|
| Rule-based | High for fixed operational rules | Apply predefined priority conditions and escalation rules. |
| LLM | High for unstructured natural-language reports | Extract information, interpret symptoms and suggest incident categories. |
| Agentic Loop | Not necessary for the initial prototype | Autonomous multi-step actions are unnecessary because human approval is required for operational decisions. |

**Selected approach: LLM + Rule-based + Human-in-the-Loop (HITL).**

This combination uses the LLM for flexible language understanding while keeping critical operational rules deterministic. Human review preserves accountability and prevents AI from independently executing real-world actions.

---

## Phase 5 — EVALUATE

### 5.1 Readiness Checklist

The following assessment is preliminary. Actual data availability, system integration and operational performance must be validated with Xanh SM stakeholders.

| Evaluation Dimension | Assessment | Evidence / Remaining Work |
|---|---|---|
| Problem clarity | Ready | The manual classification and clarification bottleneck is clearly defined as a workshop hypothesis. |
| Data availability | Needs validation | Sample incident reports, historical cases and classification labels must be obtained. |
| Data quality | Needs validation | Reports may be incomplete, inconsistent or ambiguous. A representative dataset must be reviewed. |
| Technical feasibility | Promising | LLMs can process natural-language reports; rule-based checks can enforce predefined operational boundaries. |
| Integration feasibility | Needs validation | Integration with existing driver reporting and dispatcher systems has not been confirmed. |
| Business value | Promising | Reducing manual handling time could improve dispatcher efficiency and incident triage speed. |
| Safety and governance | Requires controls | Human approval, escalation rules, access control and audit logs are necessary. |
| Evaluation readiness | Needs validation | A labeled test dataset and baseline measurements are needed to verify accuracy and handling time. |

### 5.2 Key Risks and Mitigations

| Risk | Potential Impact | Mitigation |
|---|---|---|
| Incorrect incident classification | Report sent to the wrong department | Require dispatcher approval and track classification accuracy. |
| Missing or ambiguous information | Incorrect recommendations | Ask for clarification and escalate uncertain cases to humans. |
| Failure to identify critical incidents | Delayed response to dangerous situations | Use deterministic escalation rules and prioritize human review. |
| LLM/API outage | Workflow interruption | Provide a manual fallback process. |
| Sensitive operational information exposure | Privacy and security risks | Apply access controls, data minimization and approved data-handling procedures. |

### 5.3 Proposed Pilot and Success Metrics

Before deployment, conduct a controlled pilot using historical or approved test reports.

| Metric | Proposed Target |
|---|---|
| Average handling time | Less than 2 minutes per report |
| Classification accuracy | At least 90% |
| Critical or ambiguous case escalation | 100% of identified cases routed for human review |
| Human approval | Required before operational routing |
| Fallback availability | Manual process remains available when AI is unavailable |

These are proposed pilot targets, not measured results.

### 5.4 Final Evaluation Decision

**Decision: NOT YET — Proceed to a controlled prototype and data-validation phase.**

**Rationale:**
- The problem is sufficiently clear for a prototype.
- LLM + Rule-based architecture is technically plausible.
- The potential operational value is measurable.
- However, real incident-report data, classification labels, baseline performance and integration requirements have not yet been validated.

**Conditions before a production pilot:**
1. Obtain an approved and representative sample of incident reports.
2. Define incident categories and priority rules with operational stakeholders.
3. Establish a labeled evaluation dataset.
4. Test classification accuracy and critical-case escalation.
5. Validate human approval and manual fallback procedures.

**Conclusion:** An AI Dispatcher Co-pilot is a promising solution for assisting Xanh SM dispatchers. It should initially operate as a recommendation and classification assistant, not as an autonomous dispatcher.
