# 01 — Problem Scan & Quick Problem Cards

## Phase 1 — SCAN: Opportunity Discovery

Mục tiêu: Tìm kiếm các bài toán vận hành có tiềm năng ứng dụng AI tại các công ty thành viên Vingroup thông qua 4 lenses.

| # | Subsidiary | Lens | Problem / Operational Bottleneck |
|---|---|---|---|
| 1 | VinFast | Repetitive | Phân loại yêu cầu bảo hành từ đại lý và chuyển đến bộ phận kỹ thuật phụ trách. |
| 2 | VinFast | Time-consuming | Tổng hợp báo cáo lỗi chất lượng xe từ nhiều nguồn như kiểm định, đại lý và bảo hành. |
| 3 | Xanh SM | Stakeholder Pain | Tài xế báo cáo sự cố phương tiện bằng nội dung không cấu trúc, khiến điều phối viên phải liên hệ lại để xác minh. |
| 4 | Vinhomes | AI-upgrade | Phân loại phản ánh của cư dân và chuyển đến bộ phận phụ trách phù hợp. |
| 5 | Vinpearl | Time-consuming | Tiếp nhận, phân loại yêu cầu của khách và chuyển đến bộ phận dịch vụ phù hợp. |

*Note: These are initial problem hypotheses for workshop exploration, not verified internal operational data.*

## Phase 2 — QUICK-ASSESS: Quick Problem Cards

### Card 1 — VinFast: Warranty Request Classification

**Problem:** Dealer warranty requests are received in different formats and must be manually classified and routed to the appropriate technical department.

| Field | Description |
|---|---|
| Actor | Dealer staff, warranty operators, technical department |
| Current workflow | Receive warranty request → Read and extract information → Identify issue category → Route to technical team |
| Bottleneck | Manual reading and classification of requests takes time and may lead to incorrect routing. |
| Proposed AI solution | LLM extracts vehicle information, fault codes and symptoms, then suggests an issue category and responsible department. |
| Baseline (assumption) | Approximately 10 minutes per request |
| Target | Less than 3 minutes per request; at least 90% classification accuracy |
| AI approach | LLM + Rule-based |
| Human oversight | Warranty staff review and approve the suggested classification before routing. |

### Card 2 — Xanh SM: Vehicle Incident Report Triage

**Problem:** Drivers submit vehicle incident reports using unstructured text, requiring dispatchers to clarify details and manually classify incidents.

| Field | Description |
|---|---|
| Actor | Drivers, dispatchers, technical/support teams |
| Current workflow | Driver submits incident report → Dispatcher reviews → Clarifies missing details → Classifies incident → Routes to responsible team |
| Bottleneck | Unstructured reports and missing information create repeated communication and slow down incident handling. |
| Proposed AI solution | LLM extracts location, vehicle information, time and symptoms, then suggests incident category, priority and responsible department. |
| Baseline (assumption) | Approximately 8 minutes per report |
| Target | Less than 2 minutes per report; at least 90% classification accuracy |
| AI approach | LLM + Rule-based |
| Human oversight | Dispatcher verifies the AI recommendation and confirms routing. |

### Card 3 — Vinhomes: Resident Complaint Classification

**Problem:** Resident complaints arrive through different channels and must be manually classified and forwarded to the appropriate department.

| Field | Description |
|---|---|
| Actor | Residents, customer service staff, responsible departments |
| Current workflow | Receive complaint → Read and understand content → Identify complaint category → Forward to responsible department |
| Bottleneck | Manual classification and routing can delay complaint resolution, especially when complaint descriptions are unclear. |
| Proposed AI solution | LLM identifies complaint intent, extracts key information and suggests the responsible department. |
| Baseline (assumption) | Approximately 8 minutes per complaint |
| Target | Less than 2 minutes per complaint; at least 90% classification accuracy |
| AI approach | LLM + Rule-based |
| Human oversight | Customer service staff review and approve the suggested department before forwarding. |

## Quick Assessment Summary

| Problem | Potential AI Value | Complexity | Priority |
|---|---|---|---|
| VinFast — Warranty classification | Reduce manual processing and routing time | Medium | High |
| Xanh SM — Incident report triage | Speed up incident handling and improve information extraction | Medium | High |
| Vinhomes — Complaint classification | Reduce manual classification workload | Low–Medium | Medium |

**Selected problem for Deep-Dive:**

Xanh SM — AI-assisted vehicle incident report triage.

**Reason for selection:** This problem combines unstructured natural-language input, repetitive manual classification, operational urgency and a clear human-in-the-loop boundary. It is a suitable use case for evaluating LLM + Rule-based AI assistance without giving AI autonomous authority over real-world dispatch decisions.
