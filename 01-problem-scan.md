# Problem Scan & Quick Cards

**Học viên:** Hoàng Bảo Nguyên | **Mã học viên:** 2A202603384  
**Lab:** Day 02 - AI Product Scoping | **Nhánh:** HoangBaoNguyen  
**Ngày thực hiện:** 07/11/2026

## 1. Phạm vi và mức độ bằng chứng

Bài cá nhân được chuẩn bị với trợ lý AI trong bối cảnh giả lập Vin Smart Future của đề bài. Tôi chưa phỏng vấn nhân viên hoặc tiếp cận dữ liệu nội bộ các công ty. Các pain point dưới đây là **giả thuyết discovery**; thời gian, volume và tác động kinh doanh **chưa đo**. Bản hiện tại bỏ số ước lượng do AI gán; không dùng chúng làm thống kê hoặc dự báo. Kết quả chạy phần mềm và các đầu ra model được trình bày trong mục Prototype của `02-deep-dive-report.md`.

## 2. SCAN: năm cơ hội, đủ bốn lenses

| # | Công ty / workflow giả định | Lens | Actor và bottleneck cụ thể | Cách kiểm chứng nhỏ nhất |
|---|---|---|---|---|
| P1 | Xanh SM - tiếp nhận sự cố pin trong ca điều phối | Tốn thời gian + Stakeholder Pain | Điều phối viên đọc tin nhắn, đối chiếu telemetry, kiểm tra trạm và soạn phản hồi; thiếu dữ liệu dễ dẫn đến hỏi lại nhiều lần | Xác nhận với điều phối viên; đo case được phép, cỡ mẫu do người phụ trách chốt và kiểm tra nguồn telemetry |
| P2 | Vinhomes - phân tuyến phản ánh sửa chữa | Lặp lại + AI-upgrade | BQL đọc mô tả tiếng Việt, xác định vị trí và chuyển đội xử lý; nội dung mơ hồ dễ chuyển sai tuyến | Lấy ticket có nhãn; cỡ mẫu do Data/BQL xác nhận và ma trận đội xử lý do BQL duyệt |
| P3 | Vinpearl - nhập yêu cầu đặt phòng đoàn từ email | Tốn thời gian | Nhân viên đặt phòng trích ngày, số người, loại phòng, yêu cầu đặc biệt từ email nhiều phiên bản | Đối chiếu chuỗi email ẩn danh với cỡ mẫu được xác lập với bảng nhập liệu cuối cùng |
| P4 | VinFast - đối chiếu hóa đơn sạc theo mã giao dịch | Lặp lại | Nhân viên đối soát so khớp mã, ngày, số tiền và đánh dấu chênh lệch | Chạy script join/validation trên dữ liệu mô phỏng có nhãn kiểm tra; ưu tiên Rule trước LLM |
| P5 | Xanh SM - tổng hợp nguyên nhân hủy chuyến | Stakeholder Pain + AI-upgrade | Nhân viên chất lượng đọc ghi chú tự do, gom nhóm nguyên nhân để báo cáo; khó thống nhất taxonomy | Reviewer gán nhãn độc lập trên ghi chú ẩn danh, cỡ mẫu cần xác nhận, chốt taxonomy và đo mức đồng thuận |

P4 có input và quy tắc đối chiếu ổn định nên cần thử script thông thường trước. P5 cần taxonomy và chất lượng nhãn trước khi đánh giá model. Có cơ hội tự động hóa không đồng nghĩa đã cần LLM hoặc Agent.

## 3. Quick Problem Card #1 - Xanh SM Incident Drafting

| Trường | Nội dung |
|---|---|
| Bài toán một câu | Điều phối viên cần chuẩn hóa thông tin sự cố pin và tạo bản nháp đề xuất xử lý có căn cứ, có người duyệt |
| Công ty / Actor | Xanh SM; điều phối viên là operator, tài xế là người chịu ảnh hưởng, trưởng ca chịu trách nhiệm xử lý ngoại lệ |
| Workflow hiện tại | Nhận tin → đối chiếu xe/pin → tra cứu trạm/quy trình → soạn nháp → duyệt/gửi và ghi nhận. Thời gian từng bước và tổng chưa đo |
| Bottleneck | Giả thuyết tra cứu/soạn nháp cần nhiều công; chưa có số đo tỷ trọng hoặc xếp hạng |
| Điểm AI hỗ trợ | Diễn đạt lời nhắn dễ hiểu và soạn giải thích. Rule kiểm tra pin/dữ liệu/trạm; operator quyết định hành động |
| Success metric đề xuất | Kỹ thuật đã có: raw core 3/3 qua validator; template 3/3 cùng context. Vận hành cần đo AHT, acceptance và công sửa; chưa chốt ngưỡng cải thiện |
| Kiến trúc | **Rule / workflow cố định + LLM Feature**, không cần Agent tự chọn tool |
| Boundary / fallback | Chỉ đề xuất; không gửi tin, không gọi cứu hộ thật. Telemetry thiếu/cũ hoặc output lỗi → người điều phối xử lý thủ công |
| Bằng chứng còn thiếu | Baseline thực đo, quy trình cứu hộ được phê duyệt, nguồn telemetry/trạm và đánh giá ngôn ngữ bởi operator |

## 4. Quick Problem Card #2 - Vinhomes Resident Triage

| Trường | Nội dung |
|---|---|
| Bài toán một câu | BQL cần phân loại phản ánh sửa chữa và đề xuất đội xử lý từ nội dung tự do |
| Công ty / Actor | Vinhomes; BQL, đội kỹ thuật và cư dân |
| Workflow hiện tại | Nhận ticket → đọc/xác minh vị trí → tra ma trận đội và ưu tiên → giao việc/cập nhật. Chưa đo thời gian |
| Bottleneck | Giả thuyết đọc và xác định tuyến gây khó khi ticket nhiều sự cố; chưa được xác nhận bằng dữ liệu |
| Điểm AI hỗ trợ | Trích xuất loại sự cố/vị trí và gợi ý category; rule áp ma trận đội và SLA chính thức |
| Success metric đề xuất | Đo thời gian triage, macro-F1 category và recall ca khẩn cấp trên dữ liệu có nhãn; chưa có baseline/target được xác nhận |
| Kiến trúc | LLM Feature + rule router; BQL duyệt trước giao việc |
| Boundary / fallback | Không tự đóng ticket hoặc hạ ưu tiên khẩn cấp. Thiếu dữ liệu hoặc nhiều nhãn → BQL xác minh; tình huống nguy hiểm theo quy trình hiện hành |
| Bằng chứng còn thiếu | Taxonomy, nhãn, SLA, trách nhiệm trực ban và tiêu chí đánh giá do owner xác nhận |

## 5. Quick Problem Card #3 - Vinpearl Group Email Intake

| Trường | Nội dung |
|---|---|
| Bài toán một câu | Nhân viên đặt phòng cần trích thông tin đoàn từ chuỗi email thành phiếu yêu cầu để kiểm tra |
| Công ty / Actor | Vinpearl; nhân viên đặt phòng và đối tác gửi yêu cầu |
| Workflow hiện tại | Đọc chuỗi email → xác định phiên bản mới nhất → nhập phiếu → kiểm tra và hỏi lại. Chưa đo thời gian |
| Bottleneck | Giả thuyết tổng hợp phiên bản/nhập trường cần kiểm chứng; chưa đo lỗi hoặc thời gian |
| Điểm AI hỗ trợ | Trích trường có nguồn là đoạn email; đánh dấu thiếu/mâu thuẫn. Rule kiểm tra ngày, số lượng và kiểu dữ liệu |
| Success metric đề xuất | Đo thời gian nhập và exact-match các trường quan trọng; ghi mâu thuẫn ngày/số phòng. Chưa có baseline/target được xác nhận |
| Kiến trúc | LLM extraction trong workflow cố định; nhân viên xác nhận |
| Boundary / fallback | Không tra hoặc khẳng định quỹ phòng nếu chưa có nguồn, không báo giá hay xác nhận booking thật; chuyển người khi thiếu/mâu thuẫn |
| Bằng chứng còn thiếu | Email ẩn danh, quy tắc xác định phiên bản yêu cầu và nhãn đúng của nhân viên |

## 6. Hội tụ: chọn P1 để deep-dive

Không dùng điểm số hoặc trọng số do AI tự gán để xếp hạng cơ hội.

| Candidate | Bằng chứng hiện có | Khoảng trống |
|---|---|---|
| P1 Xanh SM | Có prototype, fixture và ba raw outputs của Nguyên để kiểm tra boundary | Chưa xác nhận pain, baseline và dữ liệu doanh nghiệp |
| P2 Vinhomes | Có thẻ ý tưởng để thảo luận scope | Chưa có dữ liệu nhãn hoặc kết quả thử nghiệm trong bộ này |
| P3 Vinpearl | Có thẻ ý tưởng để thảo luận scope | Chưa có email được phép dùng hoặc kết quả thử nghiệm trong bộ này |

P1 được chọn để nghiên cứu tiếp vì có artifact và thử nghiệm kỹ thuật kiểm được, chưa phải vì đã chứng minh lợi ích kinh doanh lớn nhất. P2/P3 là phương án discovery. Việc chọn P1 cho bản nhóm là chỉ đạo trưởng nhóm đã nhận; không tự nhận đã họp/vote hoặc có thống kê khảo sát.

## 7. Phản biện trước khi xây

- **Rule có thể đủ không?** Có thể đủ cho quyết định pin/trạm và mẫu trả lời ngắn. LLM phải chứng minh cải thiện chất lượng nháp hoặc thời gian sửa so với rule + template.
- **Baseline đã có chưa?** Chưa. Cần đo với người vận hành; không dùng số AI dự đoán thay log thực.
- **Tại sao chưa cần Agent?** Các bước cố định, không cần tự chọn tool; prototype không có quyền tác động hệ thống ngoài.

## Nguồn và liên kết

- [Worksheet của lớp](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/main/01-worksheet.md): phase SCAN, QUICK-ASSESS và rubric I1.
- [Bài mẫu của lớp](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/main/02-deliverable-example.md): bối cảnh mẫu Xanh SM; bài này bổ sung phân tách telemetry/nội dung tài xế, kiểm tra dữ liệu cũ và rule guard.
- `02-deep-dive-report.md`: phân tích candidate P1 và điều kiện ra quyết định.
