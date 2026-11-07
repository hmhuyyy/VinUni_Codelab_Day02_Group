# Problem Scan & Quick Cards

**Học viên:** Hoàng Bảo Nguyên | **Mã học viên:** 2A202603384  
**Lab:** Day 02 - AI Product Scoping | **Nhánh:** HoangBaoNguyen  
**Ngày thực hiện:** 07/11/2026

## 1. Phạm vi và mức độ bằng chứng

Bài cá nhân được chuẩn bị với trợ lý AI trong bối cảnh giả lập Vin Smart Future của đề bài. Tôi chưa phỏng vấn nhân viên hoặc tiếp cận dữ liệu nội bộ các công ty. Các pain point dưới đây là **giả thuyết discovery**; thời gian, volume và mục tiêu là **giả định thiết kế**, không phải thống kê doanh nghiệp. Kết quả chạy phần mềm được dẫn riêng trong thư mục `evidence/`.

## 2. SCAN: năm cơ hội, đủ bốn lenses

| # | Công ty / workflow giả định | Lens | Actor và bottleneck cụ thể | Cách kiểm chứng nhỏ nhất |
|---|---|---|---|---|
| P1 | Xanh SM - tiếp nhận sự cố pin trong ca điều phối | Tốn thời gian + Stakeholder Pain | Điều phối viên đọc tin nhắn, đối chiếu telemetry, kiểm tra trạm và soạn phản hồi; thiếu dữ liệu dễ dẫn đến hỏi lại nhiều lần | Phỏng vấn 2 điều phối viên; đo 30 case đã ẩn danh và kiểm tra nguồn telemetry |
| P2 | Vinhomes - phân tuyến phản ánh sửa chữa | Lặp lại + AI-upgrade | BQL đọc mô tả tiếng Việt, xác định vị trí và chuyển đội xử lý; nội dung mơ hồ dễ chuyển sai tuyến | Lấy 50 ticket có nhãn và ma trận đội xử lý do BQL duyệt |
| P3 | Vinpearl - nhập yêu cầu đặt phòng đoàn từ email | Tốn thời gian | Nhân viên đặt phòng trích ngày, số người, loại phòng, yêu cầu đặc biệt từ email nhiều phiên bản | Đối chiếu 30 chuỗi email ẩn danh với bảng nhập liệu cuối cùng |
| P4 | VinFast - đối chiếu hóa đơn sạc theo mã giao dịch | Lặp lại | Nhân viên đối soát so khớp mã, ngày, số tiền và đánh dấu chênh lệch | Chạy script join/validation trên 100 dòng dữ liệu mô phỏng; ưu tiên Rule trước LLM |
| P5 | Xanh SM - tổng hợp nguyên nhân hủy chuyến | Stakeholder Pain + AI-upgrade | Nhân viên chất lượng đọc ghi chú tự do, gom nhóm nguyên nhân để báo cáo; khó thống nhất taxonomy | Hai người gán nhãn độc lập 50 ghi chú ẩn danh, chốt taxonomy và đo mức đồng thuận |

P4 có input và quy tắc đối chiếu ổn định nên cần thử script thông thường trước. P5 cần taxonomy và chất lượng nhãn trước khi đánh giá model. Có cơ hội tự động hóa không đồng nghĩa đã cần LLM hoặc Agent.

## 3. Quick Problem Card #1 - Xanh SM Incident Drafting

| Trường | Nội dung |
|---|---|
| Bài toán một câu | Điều phối viên cần chuẩn hóa thông tin sự cố pin và tạo bản nháp đề xuất xử lý có căn cứ, có người duyệt |
| Công ty / Actor | Xanh SM; điều phối viên là operator, tài xế là người chịu ảnh hưởng, trưởng ca chịu trách nhiệm xử lý ngoại lệ |
| Workflow hiện tại | Nhận tin 2 phút → đối chiếu xe/pin 2 phút → tra cứu trạm/quy trình 3 phút → soạn nháp 3 phút → duyệt/gửi 1 phút → ghi nhận 1 phút |
| Bottleneck | Tra cứu và soạn nháp: 6/12 phút giả định; lời nhắn tự do có thể thiếu pin, vị trí hoặc không khớp telemetry |
| Điểm AI hỗ trợ | Diễn đạt lời nhắn dễ hiểu và soạn giải thích. Rule kiểm tra pin/dữ liệu/trạm; operator quyết định hành động |
| Success metric đề xuất | Thời gian từ nhận tin tới hoàn tất duyệt/ghi nhận: 12 → ≤5 phút/case trên luồng đủ dữ liệu; ≥80% nháp được duyệt sau sửa nhẹ; 100% hành động cần người duyệt |
| Kiến trúc | **Rule / workflow cố định + LLM Feature**, không cần Agent tự chọn tool |
| Boundary / fallback | Chỉ đề xuất; không gửi tin, không gọi cứu hộ thật. Telemetry thiếu/cũ hoặc output lỗi → người điều phối xử lý thủ công |
| Bằng chứng còn thiếu | Baseline thực đo, quy trình cứu hộ được phê duyệt, nguồn telemetry/trạm và đánh giá ngôn ngữ bởi operator |

## 4. Quick Problem Card #2 - Vinhomes Resident Triage

| Trường | Nội dung |
|---|---|
| Bài toán một câu | BQL cần phân loại phản ánh sửa chữa và đề xuất đội xử lý từ nội dung tự do |
| Công ty / Actor | Vinhomes; BQL, đội kỹ thuật và cư dân |
| Workflow hiện tại | Nhận ticket 1 phút → đọc nội dung/xác minh vị trí 2 phút → tra ma trận đội và ưu tiên 2 phút → giao việc/cập nhật 1 phút |
| Bottleneck | Đọc và xác định tuyến: 4/6 phút giả định; một ticket có thể chứa nhiều sự cố |
| Điểm AI hỗ trợ | Trích xuất loại sự cố/vị trí và gợi ý category; rule áp ma trận đội và SLA chính thức |
| Success metric đề xuất | Thời gian triage 6 → ≤3 phút; macro-F1 category ≥0,90 trên tập có nhãn; recall sự cố khẩn cấp ≥0,99 trên tập riêng |
| Kiến trúc | LLM Feature + rule router; BQL duyệt trước giao việc |
| Boundary / fallback | Không tự đóng ticket hoặc hạ ưu tiên khẩn cấp. Thiếu dữ liệu hoặc nhiều nhãn → BQL xác minh; tình huống nguy hiểm theo quy trình hiện hành |
| Bằng chứng còn thiếu | Taxonomy, nhãn, SLA và trách nhiệm trực ban; các ngưỡng trên chưa đo được |

## 5. Quick Problem Card #3 - Vinpearl Group Email Intake

| Trường | Nội dung |
|---|---|
| Bài toán một câu | Nhân viên đặt phòng cần trích thông tin đoàn từ chuỗi email thành phiếu yêu cầu để kiểm tra |
| Công ty / Actor | Vinpearl; nhân viên đặt phòng và đối tác gửi yêu cầu |
| Workflow hiện tại | Đọc chuỗi email 4 phút → tìm thông tin mới nhất 4 phút → nhập bảng 5 phút → kiểm tra và hỏi lại 2 phút |
| Bottleneck | Tổng hợp phiên bản và nhập trường dữ liệu: 9/15 phút giả định |
| Điểm AI hỗ trợ | Trích trường có nguồn là đoạn email; đánh dấu thiếu/mâu thuẫn. Rule kiểm tra ngày, số lượng và kiểu dữ liệu |
| Success metric đề xuất | Thời gian nhập yêu cầu 15 → ≤7 phút; exact-match trường quan trọng ≥95%; mọi mâu thuẫn ngày/số phòng phải được đánh dấu |
| Kiến trúc | LLM extraction trong workflow cố định; nhân viên xác nhận |
| Boundary / fallback | Không tra hoặc khẳng định quỹ phòng nếu chưa có nguồn, không báo giá hay xác nhận booking thật; chuyển người khi thiếu/mâu thuẫn |
| Bằng chứng còn thiếu | Email ẩn danh, quy tắc xác định phiên bản yêu cầu và nhãn đúng của nhân viên |

## 6. Hội tụ: chọn P1 để deep-dive

Chấm 1-5, cao hơn thuận lợi hơn. Đây là **đánh giá giả định để chọn scope**, không phải kết quả khảo sát. Trọng số: pain 25%, khả năng có dữ liệu 25%, khả năng kiểm soát rủi ro 20%, scope hẹp 15%, khả năng prototype theo lab 15%.

| Candidate | Pain | Dữ liệu | Kiểm soát rủi ro | Scope | Prototype | Tổng /5 |
|---|---:|---:|---:|---:|---:|---:|
| P1 Xanh SM | 4 | 2 | 3 | 5 | 5 | **3,60** |
| P2 Vinhomes | 4 | 3 | 3 | 4 | 3 | 3,40 |
| P3 Vinpearl | 3 | 2 | 4 | 3 | 2 | 2,80 |

Chọn P1 vì có thể giữ phân tích và code cùng một tình huống, kiểm tra boundary trực tiếp bằng input mô phỏng và reuse khung kỹ thuật của lab. Điểm dữ liệu thấp là lý do **chưa đề xuất pilot thực địa**. P2 và P3 được giữ làm phương án để nhóm so sánh; lựa chọn cá nhân không thay quyết định chung của nhóm.

## 7. Phản biện trước khi xây

- **Rule có thể đủ không?** Có thể đủ cho quyết định pin/trạm và mẫu trả lời ngắn. LLM phải chứng minh cải thiện chất lượng nháp hoặc thời gian sửa so với rule + template.
- **12 phút là số thật chưa?** Chưa. Cần đo timestamp và thời gian xử lý tích cực của operator trước khi tuyên bố tiết kiệm.
- **Tại sao chưa cần Agent?** Các bước cố định, không cần tự chọn tool; prototype không có quyền tác động hệ thống ngoài.

## Nguồn và liên kết

- `01-worksheet.md`: phase SCAN, QUICK-ASSESS và rubric I1.
- `02-deliverable-example.md`: bối cảnh mẫu Xanh SM; bài này bổ sung phân tách telemetry/nội dung tài xế, kiểm tra dữ liệu cũ và rule guard.
- `02-deep-dive-report.md`: phân tích candidate P1 và điều kiện ra quyết định.
