# Giai đoạn 6 — Nhật ký sử dụng AI và tự phản ánh

> Bản nháp tự phản ánh dựa trên quá trình làm bài. Tôi sẽ chỉnh sửa trước khi nộp, nhất là những chi tiết chưa khớp với trải nghiệm thực tế của mình.

## Tôi đã sử dụng AI như thế nào

Tôi dùng AI như một người cùng động não để liệt kê các vấn đề vận hành tiềm năng và phát triển một vấn đề thành mô tả bài toán, quy trình, chỉ số đo lường và bản mẫu câu lệnh. AI giúp tôi sắp xếp công việc theo các vai trò, bước thực hiện, điểm nghẽn, ranh giới vận hành và trường hợp kiểm thử. Hữu ích nhất là nhờ AI phản biện xem có thực sự cần mô hình ngôn ngữ lớn hay không và ở bước nào con người cần giữ quyền kiểm soát.

## Những điều tôi phải kiểm chứng hoặc chỉnh sửa

Những gợi ý ban đầu có các con số cụ thể như số phút xử lý mỗi trường hợp và tỷ lệ hủy chuyến nhưng không có dữ liệu công ty làm bằng chứng. Tôi xem chúng là chưa được xác minh, bỏ các khẳng định về số liệu ban đầu không có căn cứ và đánh dấu những mục tiêu còn lại là giả thuyết cần đo. Tôi cũng nhận ra ý tưởng ban đầu về điểm đón của Xanh SM không khớp với tình huống pin yếu/sạc di động trong mã khung. Tôi điều chỉnh bài toán được chọn cho phù hợp với bản mẫu và đổi kiến trúc sang dùng quy tắc xác định cho ngưỡng pin và khoảng cách; mô hình ngôn ngữ lớn chỉ soạn phần giải thích.

Lần chạy đầu cũng cho thấy tệp khung chưa có phần gọi API. Sau khi bổ sung, tôi gặp lỗi phiên bản API; đổi cấu hình ứng dụng Gemini sang `v1beta` đã khắc phục lỗi đó. Khi chạy với Gemini 2.5 Flash, cả ba bài kiểm thử đối kháng đều PASS. Riêng bài kiểm thử pin yếu, mô hình trả về JSON đề xuất sạc di động đúng cấu trúc; bài kiểm thử thiếu dữ liệu yêu cầu xác minh và không khẳng định đã điều xe. Điều này cho tôi thấy kết quả tốt trên một vài ví dụ là bằng chứng hữu ích, nhưng không chứng minh câu lệnh an toàn hoặc sẵn sàng đưa vào sử dụng thực tế.

## Những điều tôi đã thay đổi

- Đánh dấu chi tiết quy trình, ước tính thời gian và số liệu tác động là giả định cho đến khi có thể kiểm tra với nhân viên vận hành và nhật ký.
- Giữ nhãn `[DRAFT_ONLY]` trong mọi phản hồi và nói rõ đề xuất điều xe không đồng nghĩa với việc xe đã được điều đi.
- Đưa ngưỡng pin và khoảng cách trạm tối đa vào quy tắc xác định, thay vì dựa vào mô hình ngôn ngữ lớn để tự tính toán an toàn.
- Thêm bài kiểm thử thiếu dữ liệu cảm biến/chèn lệnh vào câu lệnh và đặt chương trình trả về mã lỗi khác 0 khi kiểm tra thất bại. Tôi đã chạy cả ba bài kiểm thử bằng Gemini; các kiểm tra đã lập trình đều báo PASS.
- Giữ bước phê duyệt của con người và phương án thủ công dự phòng trong quy trình đề xuất.

## Tự phản ánh

AI giúp tôi nhanh chóng chuyển từ một ý tưởng rộng thành bản mẫu có thể kiểm thử, nhưng cũng khiến những giả định nghe có vẻ hợp lý dễ bị nhầm thành sự thật. Tôi cần kiểm tra các khẳng định bằng bằng chứng thực tế, dùng quy tắc cho các giới hạn an toàn nghiêm ngặt và xem đầu ra của mô hình là bản nháp. Trước khi đề xuất triển khai, tôi sẽ xác minh quy trình với những người trực tiếp thực hiện, kiểm thử các tình huống đại diện và đối kháng, rồi đo hiệu quả so với số liệu ban đầu thực tế.
