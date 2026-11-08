# Báo cáo nhóm — Vinpearl Lost-Property Intake

**Trưởng nhóm:** Hoàng Minh Huy / 2A202603495
**Repository:** VinUni_Codelab_Day02_Group · **Ngày tổng hợp:** 08/11/2026
**Candidate được chọn:** Vinpearl Lost-Property Intake, nguồn Hoàng Bảo Nguyên / 2A202603384.
**Snapshot nguồn:** `d00c86a159113530f4103a07db705f419a42a63c` · **Trạng thái:** bản nhóm để nộp trên `main`; việc nộp form lớp chưa được xác nhận.


## Thành viên và phạm vi xác nhận

| Họ tên | MSSV | Vai trò đã xác nhận |
|---|---|---|
| Hoàng Minh Huy | 2A202603495 | Trưởng nhóm |
| Bùi Quang Huy | 2A202603469 | Thành viên |
| Lê Quang Vinh | 2A202603363 | Thành viên |
| Hoàng Bảo Nguyên | 2A202603384 | Nguồn candidate được chọn |

Danh sách và trưởng nhóm do người dùng cung cấp. Trưởng nhóm đã chỉ định chọn bài Nguyên. Chưa nhận biên bản họp/đồng thuận đọc bản cuối của mọi thành viên; không gán đóng góp đã hoàn tất khi chưa được xác nhận.

## Sáu file báo cáo nhóm trên main

| File | Vai trò |
|---|---|
| [01-problem-scan.md](01-problem-scan.md) | Năm cơ hội, ba cards, phản biện và lựa chọn candidate |
| [02-deep-dive-report.md](02-deep-dive-report.md) | Báo cáo G1-G4, metric có mẫu số, nguồn và gate |
| [03-ai-log.md](03-ai-log.md) | Nhật ký tổng hợp nhóm, giúp/sai/sửa/kiểm và attribution |
| [04-workflow-diagram.pdf](04-workflow-diagram.pdf) | Current/Future-state, handoff, bottleneck cần đo, HITL/fallback |
| [05-one-page-artifact-pack.pdf](05-one-page-artifact-pack.pdf) | PS sáu trường, RACI-lite, Readiness, Decision, next experiment |
| README.md | Thành viên, hướng dẫn review và bàn giao |

Chỉ cập nhật sáu file báo cáo này. Giữ nguyên tài liệu lớp và `.py` sẵn có trên main; không merge toàn bộ nhánh cá nhân, không đưa code/keys/tests/log thô/công cụ soạn thảo vào gói nhóm. Code I2 và kết quả cá nhân giữ ở nhánh từng người. Grader cá nhân của Nguyên đã khôi phục đúng bản lớp.

## Bản đồ 60 điểm và cách review

| Gate | Điểm | Bằng chứng cần đọc |
|---|---:|---|
| G1 Workflow | 20 | Deep-Dive mục 2/2.1/2.2 và PDF trang 1: 5 bước, actor/input/output, H1-H4, loop, active/wait, cách đo |
| G2 PS | 20 | Mục 3-4/4.1: 6 trường, số đo kỹ thuật có nguồn/mẫu số, metric vận hành chưa đo, rubric Q1-Q4 |
| G3 AI Fit | 10 | Mục 5-7 và PDF trang 2: form/rule/LLM/Agent, boundary, trigger/owner/fallback, điểm dừng quyền |
| G4 Decision | 10 | Mục 8-9/12: nguồn/gap, readiness, GO synthetic / NOT YET pilot, gate có owner và stop rule |

Tập trung review G1+G2 vì chiếm 40/60 điểm; không điền số phút/volume/ROI do AI dự đoán để làm đủ bảng. Điểm 10/10 của **grader gốc cho code cá nhân** không thay điểm 60 nhóm. Section A trên main chỉ kiểm file, không chấm đủ nội dung G1-G4.

## Phân công review đề xuất — chưa phải việc đã hoàn tất

| Người | Phần việc cần nhận | Dấu vết xác nhận cần có |
|---|---|---|
| Hoàng Minh Huy | Chốt scope/Decision, điều phối đọc chéo, review diff main và form | Quyết định bản cuối và biên bản review |
| Bùi Quang Huy | Review G1: handoff/loop/cách đo | Nhận xét, lỗi đã sửa, xác nhận nội dung |
| Lê Quang Vinh | Review G2: PS/metric/mẫu số và nguồn | Nhận xét và xác nhận số nào chưa đo |
| Hoàng Bảo Nguyên | Giải thích nguồn candidate, evidence/AI Fit và prototype | Liên kết snapshot và trả lời câu hỏi về giới hạn |

Nguyên đã có bài nguồn; các nhiệm vụ review khác là đề xuất, chưa đánh dấu đã thực hiện. Mỗi thành viên vẫn cần hoàn tất bài cá nhân trên nhánh riêng theo hướng dẫn lớp.

## Bằng chứng và giới hạn

- [Nguồn bài Nguyên đã sửa](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/tree/d00c86a159113530f4103a07db705f419a42a63c): business Vinpearl; bài code I2 battery-dispatch riêng, grader nguyên bản.
- Business phụ trợ: 3/3 raw trên `gemini-3.5-flash-lite`; 9/9 field slots khớp annotation, 8 trường không-null có quote trong nguồn; 12/12 template và 92 test phụ trợ. Đây là synthetic development data, không phải hiệu quả với lễ tân.
- Code lớp của Nguyên: 82 test, raw core 3/3, grader gốc 10/10 trong điều kiện model được ghi rõ. Không nhận đây là cả nhóm chạy lại, không sử dụng điểm từ grader từng tự sửa.
- Còn thiếu business: baseline/volume/acceptance/chi phí, SOP/owner/reviewer xác nhận; giữ NOT YET pilot. Thời gian/ROI chưa đo/chưa tính.

## Checklist bàn giao và nộp bài

- [x] Có lựa chọn candidate và danh sách trưởng nhóm/thành viên từ người dùng.
- [x] Gói báo cáo theo đề tài mới, nguồn và kết quả hai phần được tách.
- [ ] Các thành viên thực sự đọc/đối chiếu, xác nhận bản cuối và phần việc.
- [ ] Trưởng nhóm xác nhận các bài cá nhân đã hoàn tất/push theo hướng dẫn lớp.
- [x] Người dùng yêu cầu phát hành trên main; phạm vi cập nhật chỉ sáu file báo cáo. Section A và diff được kiểm trước khi push; code và grader lớp giữ nguyên.
- [ ] Duy nhất Hoàng Minh Huy điền form lớp bằng tên trưởng nhóm và link repo sau khi main đã cập nhật.

Bản nhóm được phát hành trên `main` theo chỉ đạo của người dùng. Trưởng nhóm vẫn cần xác nhận việc đọc chéo và các nhánh cá nhân, sau đó điền form lớp. Báo cáo và PDF ở bảng trên là các tài liệu nộp; việc push không thay thế bước nộp form.
