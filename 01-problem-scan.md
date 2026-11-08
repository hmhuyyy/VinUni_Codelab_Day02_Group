# Phase 1 — SCAN

> Lưu ý: Đây là các giả thuyết scoping, không phải số liệu nội bộ đã được xác nhận. Cần phỏng vấn nhân viên và đo baseline trước khi dùng làm kết quả thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup
- Lặp lại
- Tốn thời gian
- AI có thể tốt hơn
- Pain từ người khác

### List bài toán của tôi

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Lặp lại | Khi xe điện gần cạn pin, tài xế và điều hành viên phải xác minh mức pin/vị trí rồi phối hợp phương án hỗ trợ sạc; cần xác minh tần suất và thời gian xử lý thực tế. |
| 2 | Xanh SM | Pain từ stakeholder | Tài xế và điều hành viên có thể mất thời gian phối hợp khi khách yêu cầu đổi điểm đón hoặc lộ trình, nhất là giờ cao điểm; cần phỏng vấn để xác nhận bottleneck. |
| 3 | VinFast | Tốn thời gian | Nhân viên có thể phải tổng hợp thủ công thông tin yêu cầu bảo dưỡng từ nhiều nguồn trước khi chuyển cho bộ phận phù hợp; cần xác minh công cụ và thời gian xử lý hiện tại. |
| 4 | Vinhomes | AI có thể tốt hơn | Yêu cầu bảo trì, khiếu nại và câu hỏi thường gặp của cư dân có thể cần đọc, phân loại và chuyển tuyến thủ công; cần đo thời gian phản hồi và tỷ lệ chuyển sai tuyến. |
| 5 | Vinmec | Pain từ stakeholder | Nhân viên tiếp nhận có thể phải nhập và chuyển thông tin hành chính giữa các bước đặt lịch; cần xác minh điểm chậm, đồng thời không để AI đưa ra quyết định chẩn đoán hay điều trị. |

---

# Phase 2 — QUICK-ASSESS

## Quick Problem Card #1

Bài toán: Khi xe Xanh SM báo pin dưới 5%, điều hành viên cần nhanh chóng xác minh thông tin và chuẩn bị phương án hỗ trợ sạc an toàn mà không khuyến nghị trạm sạc cách quá 5 km.

- Công ty thành viên: Xanh SM (đội xe điện)
- Ai đang đau (Actor)? Tài xế, điều hành viên đội xe, khách hàng đang đi trên xe
- Workflow thủ công hiện tại:
  1. Xe phát cảnh báo pin thấp
  2. Tài xế/điều hành viên xác minh mức pin và vị trí
  3. Điều hành viên kiểm tra phương án an toàn, gồm trạm sạc gần hoặc xe sạc di động
  4. Điều hành viên liên hệ tài xế và xác nhận phương án
  5. Tài xế làm theo hướng dẫn đã được xác nhận
- Bước nào tốn thời gian/lỗi nhất? Xác minh dữ liệu và phối hợp phương tiện hỗ trợ; thời gian baseline chưa được đo.
- AI có thể nhảy vào hỗ trợ ở bước nào? Sau khi nhận dữ liệu đã xác minh, AI tạo bản nháp lý do/đề xuất điều xe sạc di động khi pin dưới 5%; không tự gửi lệnh điều xe.
- Đo thành công bằng gì (Metric có số)? Mục tiêu thử nghiệm: 100% ca có pin dưới 5% không được gợi ý trạm xa hơn 5 km; giảm thời gian từ cảnh báo đến khi có phương án được nhân viên duyệt xuống dưới 2 phút. Baseline cần đo.
- Quick Architecture: Rule / State-Machine cho ngưỡng pin và khoảng cách; LLM chỉ soạn bản nháp có cấu trúc.

## Quick Problem Card #2

Bài toán: Nhân viên Vinhomes phải xử lý phản hồi cư dân về bảo trì, khiếu nại và câu hỏi thường gặp bằng thủ công, khiến thời gian phản hồi chậm và trải nghiệm cư dân giảm.

- Công ty thành viên: Vinhomes
- Ai đang đau (Actor)? Nhân viên chăm sóc cư dân, quản lý tòa nhà, cư dân
- Workflow thủ công hiện tại:
  1. Cư dân gửi yêu cầu hoặc phản hồi
  2. Nhân viên đọc và phân loại vấn đề
  3. Chuyển tới bộ phận phù hợp
  4. Soạn câu trả lời thủ công
  5. Theo dõi tiến độ xử lý
- Bước nào tốn thời gian/lỗi nhất? Phân loại yêu cầu và soạn phản hồi; giả thuyết ban đầu là 10–15 phút/ý kiến, cần đo baseline thực tế.
- AI có thể nhảy vào hỗ trợ ở bước nào? Phân loại yêu cầu, ưu tiên mức độ khẩn cấp, gợi ý câu trả lời nhanh và chuẩn hóa thông tin
- Đo thành công bằng gì (Metric có số)? Mục tiêu thử nghiệm: giảm thời gian tạo phản hồi nháp xuống dưới 3 phút và đạt ít nhất 90% phân loại đúng tuyến trên bộ kiểm thử đã được nhân viên gán nhãn; xác nhận baseline trước khi kết luận.
- Quick Architecture: LLM

## Quick Problem Card #3

Bài toán: Nhân viên Vinmec mất thời gian xác định lịch khám, kiểm tra hồ sơ và truyền thông tin bệnh nhân giữa các phòng ban, gây chậm trễ và sai sót trong quá trình khám.

- Công ty thành viên: Vinmec
- Ai đang đau (Actor)? Nhân viên lễ tân, y tá, bác sĩ, bệnh nhân
- Workflow thủ công hiện tại:
  1. Bệnh nhân đăng ký hoặc gọi đặt lịch
  2. Nhân viên kiểm tra hồ sơ và lịch khám
  3. Chuyển thông tin giữa phòng khám, phòng thu ngân và khoa liên quan
  4. Kiểm tra hồ sơ bệnh án cần thiết
  5. Xác nhận lịch và hướng dẫn bệnh nhân
- Bước nào tốn thời gian/lỗi nhất? Nhập và chuyển thông tin hành chính khi đặt lịch; giả thuyết 12–20 phút/lượt cần được xác minh. Không đưa dữ liệu bệnh án nhạy cảm vào prototype.
- AI có thể nhảy vào hỗ trợ ở bước nào? Trích xuất/tóm tắt thông tin hành chính tối thiểu và gợi ý bộ phận tiếp nhận; nhân viên xác nhận trước khi cập nhật. Không tóm tắt để chẩn đoán hoặc đề xuất điều trị.
- Đo thành công bằng gì (Metric có số)? Mục tiêu thử nghiệm: giảm thời gian xử lý hành chính xuống dưới 7 phút/lượt và đạt ít nhất 95% trường thông tin được trích xuất chính xác trên dữ liệu giả lập đã kiểm tra; đo baseline trước khi triển khai.
- Quick Architecture: LLM