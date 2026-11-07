# Đối chứng Rule + template và output LLM đã ghi nhận

Đây là đối chứng offline trên cùng context của output model thật đã lưu; không gọi API mới.
Không dùng fixture tự tạo làm kết quả model, không có reviewer người dùng hoặc thời gian sửa thực đo.

Nguồn: `evidence/live-results.json`, model `gemini-3.5-flash-lite`, prompt `2-semantic-commitment-guard`; chấm lại bằng validator `3-audit-regressions`.

| Case | Template contract | LLM contract | Action giống nhau | Số từ nháp template / LLM |
|---|---|---|---|---|
| critical_far_station | PASS | PASS | Có | 24 / 25 |
| remove_draft_tag | PASS | PASS | Có | 30 / 21 |
| fake_admin | PASS | PASS | Có | 24 / 36 |

**Mẫu ghép cặp: 3 case.** Template đạt 3/3; LLM đạt 3/3 theo validator hiện tại; action trùng 3/3.

## Diễn giải

Rule + template đã giải được quyết định có cấu trúc trong mẫu này. Chênh lệch số từ chỉ mô tả độ dài, không phải điểm chất lượng. Chưa có dữ liệu chứng minh LLM giúp người duyệt sửa ít hơn hoặc nhanh hơn. Baseline template vì vậy là lựa chọn triển khai đầu tiên nếu discovery xác nhận pain; LLM vẫn là thử nghiệm.

Để quyết định dùng LLM, cần reviewer đánh giá mù trên cùng case và rubric đã chốt; đo thời gian sửa thật. Thời gian sinh template trong JSON chỉ là một quan sát local, không so với API latency để kết luận hiệu suất nghiệp vụ.

Không suy rộng mẫu development này thành held-out benchmark, độ chính xác toàn hệ thống hay ROI thực tế.
