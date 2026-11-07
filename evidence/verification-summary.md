# Tổng hợp kiểm chứng bộ bài cá nhân

**Hoàng Bảo Nguyên | 2A202603384 | Nhánh HoangBaoNguyen**  
Thời điểm tổng hợp (UTC+07): 2026-11-07T21:29:35+07:00

## Kết quả cuối

| Kiểm tra | Kết quả | Bằng chứng |
|---|---|---|
| Offline policy/contract/SDK wiring/regression | **63/63**, không gọi model | `offline-tests.xml` |
| Bộ chấm gốc không chỉnh sửa | **10,00/10,00**, exit code 0 | `autograder-final.txt` |
| Model của lượt core cuối | **gemini-3.5-flash-lite** | `live-results.json` |
| Core live prompt v2 | **3/3 raw responses đạt validator**, 0 API error trong lượt cuối | `live-results.json` |
| Sơ đồ workflow | PDF hai trang, render và kiểm tra trực quan cả hai | `../04-workflow-diagram.pdf` |
| Tài liệu gốc / autograder | Giữ nguyên | Git diff và `environment.json` |

Bộ chấm 10 điểm là kiểm tra kỹ thuật của repo, không phải cam kết điểm nội dung 40/60. Các nháp chưa được operator thật đánh giá; mọi số liệu kinh doanh là giả định hoặc mục tiêu.

## Điều kiện model và các lượt trước

- Default trong code vẫn là **gemini-2.5-flash** theo đề. Trên model đó, ba ca lõi v1 đã chạy 3/3; output v1 sau đó bộc lộ lời hứa quá mức và suy diễn an toàn, được ghi trong AI Log.
- Prompt v2 thêm giới hạn ngữ nghĩa và regression tests. Lượt mở rộng Flash v2 nhận 1 response đạt contract, 8 API errors; không có đủ 9 responses để kết luận về cả bộ test.
- API xác nhận Flash hết quota miễn phí **20 requests/ngày**; xem `quota-diagnostic.json`. Chờ vài phút không giải quyết được quota ngày.
- **2.5 Flash-Lite** trả 404 cho tài khoản mới; lượt 0/9 không có raw response hợp lệ. Tên model còn xuất hiện trong danh sách không chứng minh generate được.
- Theo chỉ định API, dùng **3.5 Flash-Lite** bổ sung. Một lượt core trước đó có 2 responses đạt contract và 1 lỗi server 504. Sau khi thêm retry server có giới hạn, lượt cuối đạt 3/3 và autograder 10/10.
- Không gộp các model hoặc phiên bản prompt thành cùng điều kiện; không tuyên bố đã chạy đủ chín ca trên model cuối. Code khai báo 9 ca; lượt cuối xác nhận ba ca lõi.
- Timeout HTTP 11 giây, tối đa 2 attempts chỉ cho 500/502/503/504; không tự retry 400/404/429. Chi tiết trong JSON cuối. `api_error_count` là lỗi ở cấp case sau policy retry, không phải thống kê toàn bộ HTTP attempts.

## Cách đọc pass và fallback

Raw response phải đúng prefix, JSON, trường, approval và policy/trạm; không có cụm cam kết/an toàn đã bị chặn. Nếu lỗi, raw case vẫn fail, ứng dụng tạo thông báo fallback riêng để người xử lý. Validator vẫn chưa chứng minh toàn bộ ngữ nghĩa đúng; `semantic_human_review=not_performed` được giữ nguyên.

## Hạn chế và bước tiếp theo

Chưa có baseline đo thật, dữ liệu doanh nghiệp, nhãn SME, A/B với template hoặc xác nhận RACI. Quyết định báo cáo: **GO technical synthetic; NOT YET pilot thật**. Nếu lớp yêu cầu đúng Flash cho prompt cuối, chạy lại bằng model mặc định khi quota đủ; giữ log cùng phiên bản prompt. Không tự push lên GitHub trong bước chuẩn bị này.

## Bảo mật gói bàn giao

ZIP loại `.env`, `.venv`, `.git`, cache và file tạm. Key không nằm trong source hoặc evidence; `.env.example` chỉ có tên biến. `environment.json` ghi phiên bản runtime và dấu vân tay code; không ghi key.
