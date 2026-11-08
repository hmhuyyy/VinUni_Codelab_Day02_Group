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
| 1 | Xanh SM | Lặp lại | Khi điểm đón khó tiếp cận hoặc điều kiện đường thay đổi, tài xế/điều hành viên có thể phải kiểm tra và điều chỉnh phương án đón thủ công; cần xác minh tần suất và ảnh hưởng tới thời gian chờ. |
| 2 | Xanh SM | Pain từ stakeholder | Tài xế và điều hành viên có thể mất thời gian phối hợp khi khách yêu cầu đổi điểm đón hoặc lộ trình, nhất là giờ cao điểm; cần phỏng vấn để xác nhận bottleneck. |
| 3 | VinFast | Tốn thời gian | Nhân viên có thể phải tổng hợp thủ công thông tin yêu cầu bảo dưỡng từ nhiều nguồn trước khi chuyển cho bộ phận phù hợp; cần xác minh công cụ và thời gian xử lý hiện tại. |
| 4 | Vinhomes | AI có thể tốt hơn | Yêu cầu bảo trì, khiếu nại và câu hỏi thường gặp của cư dân có thể cần đọc, phân loại và chuyển tuyến thủ công; cần đo thời gian phản hồi và tỷ lệ chuyển sai tuyến. |
| 5 | Vinmec | Pain từ stakeholder | Nhân viên tiếp nhận có thể phải nhập và chuyển thông tin hành chính giữa các bước đặt lịch; cần xác minh điểm chậm, đồng thời không để AI đưa ra quyết định chẩn đoán hay điều trị. |

---

# Phase 2 — QUICK-ASSESS

## Quick Problem Card #1

Bài toán: Hệ thống điều phối xe Xanh SM gợi ý điểm đón và điểm giao không chính xác, khiến tài xế phải điều chỉnh thủ công và làm tăng thời gian chờ, tỷ lệ hủy chuyến.

- Công ty thành viên: Xanh SM
- Ai đang đau (Actor)? Tài xế, điều hành viên, khách hàng, bộ phận vận hành
- Workflow thủ công hiện tại:
  1. Nhận yêu cầu đặt xe hoặc đổi lộ trình
  2. Kiểm tra vị trí hiện tại và nhu cầu chuyến đi
  3. Hệ thống đề xuất điểm đón/điểm giao
  4. Tài xế điều chỉnh thủ công nếu không hợp lý
  5. Chuyển lại cho điều hành viên xác nhận
- Bước nào tốn thời gian/lỗi nhất? Điều chỉnh thủ công lộ trình và điểm đón trong giờ cao điểm; trung bình 8–12 phút/chuyến
- AI có thể nhảy vào hỗ trợ ở bước nào? Đề xuất điểm đón phù hợp theo thời gian thực, phân tích lưu lượng, dự đoán điểm đón hợp lý trước khi tài xế chỉnh sửa
- Đo thành công bằng gì (Metric có số)? Mục tiêu thử nghiệm: giảm thời gian xử lý điều chỉnh từ baseline đo được xuống dưới 2 phút; giảm tỷ lệ hủy/lệch lộ trình ít nhất 20% so với baseline. Các con số 8–12 phút và tỷ lệ hiện tại cần được kiểm chứng bằng log hoặc quan sát.
- Quick Architecture: Rule (tối ưu tuyến/điểm đón); có thể dùng LLM phụ trợ để tóm tắt yêu cầu bằng ngôn ngữ tự nhiên.

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