# AI Log của quá trình tổng hợp nhóm

**Trưởng nhóm:** Hoàng Minh Huy / 2A202603495
**Repository:** VinUni_Codelab_Day02_Group · **Ngày tổng hợp:** 08/11/2026
**Candidate được chọn:** Vinpearl Lost-Property Intake, nguồn Hoàng Bảo Nguyên / 2A202603384.
**Snapshot nguồn:** `d00c86a159113530f4103a07db705f419a42a63c` · **Trạng thái:** bản nhóm để nộp trên `main`; việc nộp form lớp chưa được xác nhận.


## 1. Attribution và việc thực sự đã diễn ra

Người dùng chỉ định lấy bài Nguyên và cung cấp bốn họ tên/MSSV, xác nhận Hoàng Minh Huy là trưởng nhóm. Trợ lý tổng hợp Markdown, PDF, hướng dẫn trưởng nhóm, rà số và mô phỏng áp dụng main local. Không nhận đã có cuộc họp, mọi người đọc bản cuối, phỏng vấn operator hoặc doanh nghiệp phê duyệt.

Nguồn chính: [bài cá nhân Nguyên đã khắc phục lỗi grader/prototype](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/tree/d00c86a159113530f4103a07db705f419a42a63c). Không chuyển reflection ngôi “tôi” của Nguyên thành trải nghiệm của cả nhóm. Những người khác chưa được gán việc đã làm nếu chưa xác nhận; phân công review trong README là đề xuất.

## 2. Nhật ký giúp / sai / sửa / kiểm

| Đầu vào có thật | AI hỗ trợ | Cách kiểm và giới hạn |
|---|---|---|
| Trưởng nhóm chọn bài Nguyên, dặn chưa push | Chuyển nguồn đã sửa thành bản nhóm Vinpearl | Không thay main/nhánh cá nhân, chỉ chuẩn bị gói local |
| Danh sách và trưởng nhóm do người dùng cung cấp | Điền metadata đúng người/MSSV | Không suy danh tính/đóng góp từ username |
| Yêu cầu không dùng AI dự đoán số liệu | Giữ metric có log, để business chưa đo | Replay 3 raw/9 slots/8 quote; không gán thời gian/volume/ROI |
| Rubric G1-G4 | Bổ sung handoff, loop, active/wait, mẫu số và stop rule | Không dùng kiểm file hoặc code10/10 thay chấm nội dung60 |
| Template đã qua các fixture | Phản biện giá trị tăng thêm LLM | Form/rule ưu tiên, chưa kết luận LLM tạo hiệu quả |
| Sai phạm vi code/grader ở phiên trước | Kế thừa bản cá nhân đã sửa đúng | Bài code cố định tách khỏi business, grader nguyên bản; không mang `.py` cá nhân vào main |
| Người dùng sau đó yêu cầu push bản nhóm lên main | Cập nhật trạng thái bàn giao và chuẩn bị commit sáu file báo cáo | Kiểm Section A và diff trước khi push; giữ nguyên code, grader và các nhánh cá nhân |
| Người học xác nhận chưa có dữ liệu thực tế và yêu cầu không AI dự đoán | Làm rõ phần G1-G2 chưa có bằng chứng, bổ sung phiếu thu và định nghĩa metric; thống nhất RACI | Replay raw và 12 template offline, đếm lại XML kiểm thử; không tạo thời gian/impact/target giả |

## 3. Những kết luận AI không được tự tạo

- Không gọi source quote là xác nhận vật thật/chủ sở hữu hoặc chất lượng ngữ nghĩa hoàn hảo.
- Không dùng kết quả synthetic làm accuracy, SLA hoặc ROI của Vinpearl.
- Không giữ điểm 10 từ grader tự sửa làm điểm lớp; source đã khôi phục grader gốc, điểm kỹ thuật cá nhân vẫn khác điểm nhóm.
- Không gọi thay model do quota là đã thực hiện đủ đúng 2.5 Flash. Model/lượt/log được ghi riêng.
- Không dựng biên bản họp, chữ ký, SME labels hoặc đóng góp chưa có căn cứ.

## 4. Reflection của bản tổng hợp

Điểm đáng giữ là chọn scope hẹp và sẵn sàng NOT YET khi thiếu dữ liệu/owner, kiểm form/rule trước LLM, tách quyền soạn phiếu khỏi quyền ghi sổ/trả đồ. Nhóm cần dùng bản này để đọc chéo và hiểu quyết định, không thay việc thành viên tự giải thích bài của mình.

3 raw business/12 template/92 tests phụ trợ được kế thừa từ Nguyên; 82 tests và grader gốc10/10 là phần code lớp riêng. Trợ lý rà lại raw/template offline khi tổng hợp; không có lời gọi Gemini mới hoặc vận hành thật trong việc dựng gói nhóm. Chưa có operator review, baseline hoặc khảo sát tập thể.

Lượt đối chiếu thống kê giữ nguyên log gốc: 3/3 case, 9/9 field slots gồm một null đúng, 8/8 quote không-null, 1/1 field thiếu và 12/12 template khớp. Đếm lại JUnit có 92 test phụ trợ và 82 test code lớp, tổng 174 test offline; không nhận đã chạy thêm 174 lượt model. RACI bản một trang được sửa: Ops owner là A, lễ tân/trưởng ca là R ở duyệt/ghi nhận, đồng nhất mục 7 báo cáo. G1-G2 còn thiếu số liệu nghiệp vụ thật; NOT YET vẫn có hiệu lực.

## 5. Trạng thái bàn giao

Sáu file báo cáo được phát hành trên main theo yêu cầu mới của người dùng. Cần các thành viên xác nhận bản cuối và hoàn tất nhánh cá nhân; chưa có xác nhận đã nộp form. Trưởng nhóm Hoàng Minh Huy là người đại diện điền form lớp bằng link repo sau khi kiểm tra bản main. Việc công bố không được ghi thành bằng chứng đã họp nhóm, đã có operator review hoặc đã nộp form.
