# Problem Scan — năm cơ hội mới và ba Quick Cards

**Học viên:** Hoàng Bảo Nguyên / **MSSV:** 2A202603384
**Ngày:** 08/11/2026 / **Nhánh cá nhân:** `HoangBaoNguyen`
**Đề tài:** Vinpearl Lost-Property Intake — chuẩn hoá phiếu đồ nhặt được.


## 1. Phạm vi và nguồn

**Phạm vi file này là business Vinpearl.** Thử nghiệm lost-property được dùng làm bằng chứng phụ trợ; bài code cố định I2 vẫn là battery-dispatch trong `starter-code/prompt_prototype.py`, chấm bằng grader gốc.

Không sử dụng bài toán sự cố pin của worked example. Năm pain points sau là giả thuyết discovery, không phải kết quả phỏng vấn. Không có thời gian/volume/chi phí hoặc tỷ lệ cải thiện do AI dự đoán. Chỉ P1 có nguồn công khai xác nhận sự tồn tại của nhiệm vụ đồ thất lạc; workflow chi tiết và pain vẫn cần xác minh.

## 2. SCAN — đủ bốn lenses

| Mã | Đơn vị / bài toán | Lens | Actor và bottleneck cần kiểm chứng | Cách xác minh |
|---|---|---|---|---|
| P1 | Vinpearl: chuẩn hoá phiếu đồ nhặt được từ ghi chú bàn giao | Tốn thời gian + Stakeholder Pain | Lễ tân đọc ghi chú, tách mô tả/nơi/thời điểm; thiếu hoặc mâu thuẫn có thể gây hỏi lại | Xem biểu mẫu được phép, quan sát bàn giao và xác minh lỗi thật |
| P2 | Vinpearl: đối soát đồ vải giao nhận giữa kho và bộ phận buồng | Lặp lại | Nhân viên kho so mã/chủng loại/số lượng, tách chênh lệch cần người xác nhận | Kiểm phiếu giao nhận ẩn danh; thử join/rule trước |
| P3 | Vinpearl: chuẩn hoá yêu cầu thiết bị phòng hội nghị từ email | AI-upgrade + Tốn thời gian | Điều phối sự kiện tách tên thiết bị, bố trí và yêu cầu còn thiếu, tránh lẫn phiên bản | So email được phép với phiếu setup do nhân viên duyệt |
| P4 | VinFast: lập checklist hồ sơ giao nhận phụ tùng từ ghi chú kho | Lặp lại | Nhân viên kho dò mã lô/chứng từ thiếu, có nguy cơ bỏ sót trường cần hỏi lại | Xác nhận mẫu hồ sơ và rule hiện hành với người phụ trách |
| P5 | VinUni: gom câu hỏi trước buổi thực hành thành agenda hỗ trợ | Stakeholder Pain | Trợ giảng gom câu hỏi trùng/thiếu ngữ cảnh trước buổi lab | Dùng câu hỏi không chứa định danh, đối chiếu với agenda trợ giảng chốt |

## 3. Card P1 — Lost-Property Intake (được chọn)

| Trường | Nội dung |
|---|---|
| Bài toán / actor | Lễ tân cần chuyển ghi chú đồ nhặt được thành phiếu nháp có nguồn và câu hỏi làm rõ |
| Đơn vị | Vinpearl; người nhặt/nhân viên khu vực cung cấp ghi chú, lễ tân kiểm, trưởng ca xử lý ngoại lệ |
| Workflow hiện tại, 5 bước | Nhận ghi chú → kiểm trường/căn cứ → nhập phiếu → hỏi lại phần thiếu/mâu thuẫn → người duyệt và ghi sổ |
| Bottleneck | Tách trường/đối chiếu và vòng hỏi lại là giả thuyết; thời gian từng bước và tổng chưa đo |
| Điểm hỗ trợ | Trích ba trường nguyên văn, gắn evidence, đánh dấu thiếu; người quyết định nội dung cuối |
| Metric có số đã đo | 12/12 fixture template; 3/3 raw core model thay thế khớp annotation synthetic. AHT/acceptance/chi phí thực chưa đo |
| Kiến trúc | Rule/biểu mẫu là baseline; LLM Feature thử cho ghi chú tự do; chưa cần Agent |
| Boundary | Không suy chủ sở hữu, thêm liên hệ, trả/gửi đồ hoặc ghi sổ thật. Thiếu/mâu thuẫn → người xác minh |
| Còn thiếu | Biểu mẫu/SOP được phép, dữ liệu đã xử lý định danh, baseline, reviewer và owner xác nhận |

## 4. Card P2 — Đối soát đồ vải

| Trường | Nội dung |
|---|---|
| Bài toán / actor | Nhân viên kho/buồng cần chỉ ra chênh lệch phiếu giao nhận đồ vải |
| Workflow hiện tại, 4 bước | Nhận hai phiếu → so mã/chủng loại → so số lượng → người xác minh và chốt chênh lệch |
| Bottleneck | Sai khác phiên bản/mã là giả thuyết; chưa có quan sát hay thống kê lỗi |
| Điểm hỗ trợ | Chuẩn hoá mã theo danh mục, join và rule số lượng; không cần LLM nếu đã có cấu trúc |
| Metric | Số dòng đối chiếu đúng / dòng có nhãn, số chênh lệch bị bỏ sót, công xác minh; chưa đo, chưa tự đặt target |
| Kiến trúc | Rule + bảng tính/script trước; No-Go LLM nếu không có tác vụ ngôn ngữ cần thiết |
| Boundary | Không tự điều chỉnh tồn kho hoặc quy trách nhiệm nhân viên; ngoại lệ cần người duyệt |

## 5. Card P3 — Yêu cầu thiết bị hội nghị

| Trường | Nội dung |
|---|---|
| Bài toán / actor | Điều phối sự kiện cần phiếu nháp thiết bị/bố trí từ email khách và phiên bản sửa |
| Workflow hiện tại, 5 bước | Nhận email → xác định phiên bản → tách thiết bị/bố trí → làm rõ phần thiếu → nhân viên duyệt phiếu setup |
| Bottleneck | Đọc nhiều phiên bản và yêu cầu mơ hồ là giả thuyết; chưa đo thời gian |
| Điểm hỗ trợ | Trích yêu cầu kèm đoạn email nguồn, ghi mâu thuẫn; rule so danh mục thiết bị |
| Metric | Field exact-match trên annotation, mâu thuẫn được phát hiện, thời gian sửa; chưa có số đo/target xác nhận |
| Kiến trúc | LLM extraction trong workflow cố định + rule; template nếu khách dùng form chuẩn |
| Boundary | Không hứa thiết bị còn hàng, báo giá, đặt dịch vụ hoặc gửi xác nhận; nhân viên chốt khả dụng |

## 6. Lựa chọn và phản biện

Chọn P1 làm candidate cá nhân mới: có nguồn công khai về nhiệm vụ, đầu ra hẹp và có thể kiểm source-evidence trên synthetic notes. Không xếp hạng bằng điểm/trọng số AI tự gán; chưa khẳng định P1 có lợi ích lớn nhất hoặc pain đã được khách sạn xác nhận.

- **Ops:** ghi chú được trích đúng chưa chắc món đồ tồn tại hoặc thuộc người nhận. Phạm vi dừng ở phiếu nháp; kiểm vật lý/quyền sở hữu nằm ngoài prototype.
- **CFO:** biểu mẫu chuẩn/rule có thể đủ. Template đã qua cả 12 fixture nên chưa chứng minh giá trị tăng thêm của LLM.
- **Data:** synthetic annotations do trợ lý soạn, chưa có reviewer nghiệp vụ. Không suy ra accuracy vận hành hoặc tiết kiệm từ mẫu này.
- **Điều kiện đổi quyết định:** không có pain/log/quyền dữ liệu → NOT YET; form/rule đáp ứng tốt → bỏ LLM.

Nguồn: [Vinpearl — Trưởng Bộ phận Tiền sảnh](https://careers.vinpearl.com/job/vinpearl-nha-trang-truong-bo-phan-tien-sanh-4416), nhiệm vụ liên quan đồ thất lạc/nhặt được, đọc 08/11/2026. Đây là mô tả công việc công khai, không phải nghiên cứu thời gian/volume. [Worksheet lớp](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/9ad1a44e43eb21162229831bad6c38dfc69ade0d/01-worksheet.md) cung cấp lenses/cards/rubric. Các candidate P2-P5 chưa có dữ liệu doanh nghiệp xác nhận.
