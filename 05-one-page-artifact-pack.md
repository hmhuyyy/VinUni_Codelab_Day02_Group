# Artifact pack - bản nội dung cho một trang PDF

**Hoàng Bảo Nguyên / 2A202603384 / Day 02 / 07-11-2026**

**Use case:** Xanh SM - chuẩn hóa thông tin sự cố pin và soạn nháp cho điều phối viên. Bối cảnh và baseline là giả định discovery; dữ liệu kiểm thử là mô phỏng.

## Problem Statement

| Trường | Tóm tắt |
|---|---|
| Actor | Điều phối viên tiếp nhận sự cố; trưởng ca duyệt ngoại lệ; tài xế nhận phản hồi |
| Workflow | Nhận tin → xác minh pin/độ mới → tra quy trình/trạm → soạn → duyệt/gửi → ghi log; baseline giả định 12 phút/case |
| Bottleneck | Tra cứu + soạn nháp: 6/12 phút; nội dung thiếu hoặc không khớp telemetry |
| Impact | Giả định 12 case/ngày ×26 ngày =312 case/tháng; 62,4 giờ xử lý theo case, chưa là số liệu hoặc thiệt hại đã đo |
| Success | Mục tiêu ≤5 phút/case đủ dữ liệu; ≥80% nháp chấp nhận sửa nhẹ; mọi hành động có người duyệt; báo cả fallback, chất lượng và API lỗi |
| Boundary | Rule quyết định nhánh từ context; LLM chỉ nháp. Không gửi tin/điều xe thật, không bịa trạm hoặc suy ra khả năng lái an toàn. Thiếu/cũ/lỗi → người xử lý |

## RACI-lite

| Hoạt động | R - thực hiện | A - chịu trách nhiệm | C - tham vấn |
|---|---|---|---|
| Problem / metric | Operator | Ops owner | AI / Data |
| Build / eval | AI / Data | Ops owner | Operator / Risk |
| Duyệt / hành động | Operator | Trưởng ca | Risk khi ngoại lệ |
| Dừng AI / rollback | Operator / Platform | Ops owner | AI / Risk |

## AI Readiness và quyết định

Có fixture, code rule/prompt/validator và evidence kỹ thuật. Chưa có baseline/log thật, nhãn SME, đánh giá operator, A/B thời gian sửa hoặc owner nhận trách nhiệm vận hành.

**GO:** prototype synthetic. **NOT YET:** pilot thật. **NO-GO cho LLM** nếu template đạt chất lượng tương đương với công sức/chi phí thấp hơn. Kiến trúc: workflow cố định + rule, thử LLM feature; chưa cần Agent.

## Next experiment nhỏ nhất

Trong hai ngày làm việc theo kế hoạch: (1) xác nhận workflow và đo 30 case ẩn danh; (2) chốt policy/RACI, chuẩn bị nhãn; (3) so template/LLM trên cùng case bằng rubric Q1-Q4 và thời gian sửa thật; (4) chỉ mở shadow pilot khi gate đạt, owner xác nhận và rollback đã thử. Không triển khai hành động tự gửi.

Kết quả kỹ thuật và model thực chạy đọc tại `evidence/submission-verification.md`. Đối chứng ba output đã lưu: template và LLM đều đạt contract; chưa chứng minh LLM có giá trị hơn cho người dùng. Các mục tiêu kinh doanh chưa được đo.
