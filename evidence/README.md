# Cách đọc bằng chứng thực thi

Đọc **`submission-verification.md`** cho phiên bản sẵn sàng nộp. `verification-summary.md` và `environment.json` là snapshot lịch sử trước audit. Evidence dùng dữ liệu mô phỏng, không có dữ liệu khách hàng hoặc API key. Không gộp model, prompt hoặc validator khác nhau thành cùng điều kiện.

| File | Ý nghĩa |
|---|---|
| `offline-tests.xml` | JUnit XML của các test offline: policy edges, output bị sửa, fallback, mock SDK và regression; không phải model output |
| `live-probe.json` | Lượt đầu lỗi cấu hình timeout |
| `live-initial-config-error.json` | Lượt đầu lỗi cấu hình API version và quota; không có bằng chứng model vượt boundary |
| `live-probe-fixed.json` | Probe sau sửa API version gặp HTTP 429 |
| `live-core-results.json` | Ba ca lõi prompt v1, trước khi bổ sung kiểm tra cam kết ngữ nghĩa |
| `live-extended-results.json` | Chín ca prompt v1: có output lịch sử dùng để phát hiện lời hứa quá mức; một API error |
| `live-injection-retry.json` | Retry một ca v1 gặp 429; giữ dấu vết lỗi dịch vụ |
| `live-injection-v2.json` | Probe v2 gặp quota; không tính là model pass |
| `live-core-v2-quota.json` | Lượt bộ chấm gặp quota; giữ để giải thích kết quả ban đầu |
| `autograder-quota-limited.txt` | Log bộ chấm tương ứng với lượt quota-limited |
| `live-extended-v2-results.json` | Lượt mở rộng cuối với prompt v2; SHA-256 prompt và nhịp gọi ghi trong JSON |
| `live-results.json` | Ba ca do lượt autograder cuối thực thi, prompt v2 |
| `live-extended-flash-lite-results.json` | Lượt 2.5 Flash-Lite bị HTTP 404; không tính là model pass |
| `live-model-availability-probe.json` | Probe đầu trên 3.5 Flash-Lite được dịch vụ chỉ định thay thế |
| `model-availability-diagnostic.json` | Ghi lại phản hồi 404 của 2.5 Flash-Lite và tên model API chỉ định |
| `quota-diagnostic.json` | Thông báo đã che key: Flash hết quota miễn phí 20 requests/ngày |
| `live-core-flash-daily-quota.json` | Core Flash bị chặn bởi quota ngày trước khi đổi cấu hình local sang Lite |
| `autograder-flash-daily-quota.txt` | Bộ chấm trên Flash khi quota ngày đã hết |
| `autograder-final.txt` | Log nguyên bản bộ chấm gốc ở lượt cuối |
| `live-core-lite-server-error.json` | Lượt 3.5 Flash-Lite trước retry: 2 responses đạt contract, 1 lỗi server 504 |
| `autograder-lite-server-error.txt` | Log bộ chấm của lượt server-error trước khi thêm retry |
| `environment.json` | Phiên bản Python/thư viện, commit template và dấu vân tay mã nguồn cuối |
| `offline-tests-submission.xml` | 82 tests của phiên bản đã sửa sau audit |
| `autograder-submission.txt` | Lượt bộ chấm gốc mới sau khi sửa audit |
| `live-core-before-submission.json` | Giữ nguyên output core trước lượt xác nhận mới |
| `template-comparison.json` / `.md` | Đối chứng offline giữa template và ba output model đã ghi; không có API mới |
| `submission-environment.json` | Metadata và dấu vân tay mã nguồn phiên bản sẵn sàng nộp |
| `audit-sol61-bb1f3bd.md` | Audit độc lập của snapshot cũ; không phải điểm của phiên bản đã sửa |

`passed` là số raw responses đáp ứng validator của đúng phiên bản đó. `api_error_count` và `contract_violations` được tách riêng ở bản v2. Nếu có API error, chưa được coi ca đó đã kiểm tra hành vi model. Fallback được ghi riêng, không làm response lỗi trở thành pass.

Không khẳng định tỷ lệ lỗi ngoài mẫu, semantic review của người vận hành, SLA doanh nghiệp hoặc tiết kiệm tiền mặt từ những file này. `semantic_human_review` vẫn là `not_performed` cho tới khi có operator thật đánh giá.
