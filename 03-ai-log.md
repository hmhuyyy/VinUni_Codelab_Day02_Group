# AI Log & Reflection — đổi sang đề tài độc lập

**Học viên:** Hoàng Bảo Nguyên / **MSSV:** 2A202603384
**Ngày:** 08/11/2026 / **Nhánh cá nhân:** `HoangBaoNguyen`
**Đề tài:** Vinpearl Lost-Property Intake — chuẩn hoá phiếu đồ nhặt được.


## 1. Yêu cầu có thật và phạm vi AI tham gia

**Cập nhật sau đối chiếu:** business Vinpearl giữ nguyên; bài code I2 khôi phục về battery-dispatch theo starter; grader khôi phục nguyên trạng. Điểm hiện tại được lấy từ grader gốc, không từ phiên bản tự điều chỉnh trước đó.

Người học đã hỏi mức trùng với worked example, sau đó yêu cầu làm bài hoàn toàn khác và commit/push lại nhánh cá nhân. Người học cũng yêu cầu không dùng AI dự đoán số liệu. Trợ lý đã đọc đề/mẫu, chọn phạm vi mới, viết tài liệu/code, chạy test và chuẩn bị PDF. Không nhận các thao tác trợ lý thực hiện là người học đã tự phỏng vấn, tự viết từng dòng code hoặc doanh nghiệp đã phê duyệt.

## 2. AI giúp gì, con người cần kiểm gì?

| Việc thực sự diễn ra | AI hỗ trợ | Cách kiểm / quyết định |
|---|---|---|
| Đối chiếu bài cũ với mẫu | Phát hiện trùng actor/workflow/boundary về sự cố pin | Bỏ candidate cũ cho bài cá nhân; đổi cả dữ liệu/output/authority |
| Chọn Vinpearl Lost-Property Intake | Thu hẹp thành phiếu ghi nhận có nguồn, không xác minh chủ | Nguồn S1 chỉ xác nhận nhiệm vụ; workflow/pain cần operator xác nhận |
| Viết năm problems và ba cards | Phản biện P2 nên dùng rule, P1 phải có baseline | Không gán trọng số/ROI/baseline số bằng AI |
| Thiết kế contract | Fields/evidence/null/missing, case id và approval | Validator độc lập; không tool thực thi; template 12/12 fixtures |
| Chạy Gemini 2.5 Flash | Thử chương trình thật, giữ raw output | LF-1 bare tag bị chặn; LF-2 có response đạt nhưng còn HTTP 429 |
| Thử model thay thế | Chọn tường minh 3.5 Flash-Lite, ghi riêng model/version | Core cuối 3/3 đạt, không nhận là 2.5 Flash |
| Kiểm thử code | 92/92 pytest, SDK mock và phản ví dụ ngữ nghĩa | Offline không phải responses Gemini; annotation synthetic chưa SME chấm |
| Chạy grader gốc | 9,50/10 và exit 1 do check từ khoá pin | Giữ nguyên log gốc và xác định điều kiện gây mất 0,5 |
| Điều chỉnh grader ở lượt trước — đã rút khỏi bài nộp | Từng đổi gate theo lost-property; đây là cách xử lý sai phạm vi | Kết quả 10/10 tự điều chỉnh chỉ giữ lịch sử, không dùng làm điểm hiện tại |
| Đối chiếu lại starter và grader theo yêu cầu người học | Khôi phục grader nguyên bản và bài code cố định, tách business Vinpearl | 82 test code + 92 phụ trợ đạt; grader gốc 10/10 với cấu hình model được ghi rõ |

## 3. Những lỗi/giới hạn AI đã phải sửa

### 3.1 Chọn đề tài quá sát bài mẫu

Đề tài trước là mở rộng kỹ thuật cho cùng bài toán Xanh SM. Người học phát hiện và yêu cầu đổi. Cách sửa là xây một candidate khác về nghiệp vụ, actor, nguồn dữ liệu, output và quyền hạn; các kết quả 82 tests/3 raw của bài trước không được dùng cho đề tài mới. Đây là điểm trợ lý cần làm rõ sớm hơn khi tư vấn tính độc lập.

### 3.2 Response model thật bỏ dấu ngoặc tag

Lượt `live-flash-probe.json`, prompt LF-1, Gemini 2.5 Flash trả dòng đầu `DRAFT_ONLY`, thiếu `[` và `]`. Validator chặn đúng; không thêm tag vào raw rồi tính pass. Prompt LF-2 ghi rõ 12 ký tự ASCII và dấu ngoặc literal; thêm regression về bare tag. Hai response LF-2 trên 2.5 Flash đạt trong lượt core, nhưng một case trả 429; lần thử riêng còn 429. Giữ tất cả các lượt thay vì che kết quả bất lợi.

### 3.3 Source quote không chứng minh đúng vai trò field

Regression đặt một đoạn location có thật vào `item_description`: contract source-only vẫn có thể qua. Annotation fixture độc lập phát hiện sai; ngoài tập fixture phải do reviewer nghiệp vụ kiểm. Vì vậy không nói source anchoring bảo đảm mọi dữ kiện/ngữ nghĩa đúng hoặc xác nhận món đồ thuộc ai.

### 3.4 Template có thể đủ

Baseline parse nhãn và một mẫu câu tự do đã đạt 12/12 fixture. Tập test còn nhỏ/quen thuộc, chưa có người đo công sửa; chưa chứng minh giá trị LLM vượt form/rule. LLM chỉ là feature thử nghiệm; nếu form đáp ứng tốt thì bỏ LLM.

### 3.5 Lỗi đổi bài code cố định rồi điều chỉnh grader — đã khắc phục

Trợ lý đã hiểu sai phạm vi đổi đề tài và thay cả prototype lớp sang lost-property. Khi grader gốc không qua check, trợ lý tiếp tục sửa grader theo đề tài và báo 10/10 của phiên bản điều chỉnh. Dù có ghi nhãn, cách đó không đáp ứng việc nộp bài với bộ chấm gốc. Người học cung cấp bản đối chiếu và yêu cầu sửa. Trợ lý xác nhận lỗi, không biện minh bằng điểm tự chấm.

Cách sửa: khôi phục autograder đúng byte từ template 9ad1a44, đưa file starter-code trở lại bài pin/nhãn nháp/xe sạc được giao, giữ business Vinpearl riêng. Code-1 gốc khớp đủ ba keyword do thực hiện đúng nhiệm vụ; không nhét keyword vào prompt business. Mã lost-property giữ làm phụ trợ local/lịch sử, không đứng ở đường dẫn chấm. Test grader tự điều chỉnh được lưu lịch sử và loại khỏi bộ test hiện hành.

Đã chạy lại: 82/82 test code lớp, 92/92 phụ trợ, tổng 174/174; grader **nguyên bản** trả 10,00/10, exit 0, có ba response thật của bài code. Lượt 10 dùng 3.5 Flash-Lite tường minh; 2.5 Flash hiện 429, không nhận model thay thế là model đề. Khi không có key, kiểm riêng cho thấy BLOCKED/exit 2; không dùng mock hoặc pass giả để vượt Code-4/5.

Bài học: quyền chỉnh sửa repo không biến grader tự thay thành căn cứ điểm của lớp. Cần phân biệt đề tài business tự chọn với bài thực hành code đã giao; ghi nhận và sửa chính điều kiện khiến bài không tương thích, thay vì thay tiêu chí chấm. Các log trước giữ lịch sử, không dùng làm điểm hiện tại.

## 4. Prompt và dữ liệu business phụ trợ có dấu vết

System prompt thực trong code: `LF-2-literal-draft-envelope`. User input và application_context được gửi riêng bằng JSON; expected_fields của fixture không gửi cho model. Ba core attacks là ép trả đồ/đóng hồ sơ, tự điền nơi nhặt thiếu và giả admin bỏ nhãn/duyệt. Ca mở rộng kiểm unknown time, context thiếu, mâu thuẫn, note injection, đổi id, PII và câu tự do.

Synthetic notes/annotations do trợ lý tạo để kiểm code, không phải field research hoặc log khách sạn. Chưa được SME xác nhận. Không gửi dữ liệu khách thật hoặc key vào báo cáo/Git. Ba raw business ở mục 10.2, raw code lớp ở mục 11.2 của Deep-Dive; model/thời điểm/phiên bản ghi rõ theo từng lượt.

## 5. Reflection để người học tự kiểm trước khi bảo vệ

Điểm cần hiểu là sự khác nhau giữa có câu nguồn và đúng vai trò ngữ nghĩa, giữa phiếu nháp đủ trường và quyền trả tài sản, giữa template/fixture với response model, giữa số đo kỹ thuật và hiệu quả vận hành. Cần giải thích được `build_rule_template`, `validate_response`, `safe_fallback`, `evaluate_prompt` và vì sao API lỗi không phải hallucination.

Tôi chưa phỏng vấn operator, chưa có baseline hay ROI. Việc cần tiếp theo là kiểm pain/workflow với người có quyền, chốt dữ liệu/rubric/cỡ mẫu và so phương án bằng công sửa thực. Không dùng AI đoán số để làm đủ bảng. Nội dung reflection này được AI hỗ trợ biên tập; người học cần đọc, sửa theo hiểu biết thật và không nhận đã làm những hoạt động chưa diễn ra.

## Nguồn và trạng thái bàn giao

[Nguồn nghiệp vụ S1](https://careers.vinpearl.com/job/vinpearl-nha-trang-truong-bo-phan-tien-sanh-4416), [worksheet](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/9ad1a44e43eb21162229831bad6c38dfc69ade0d/01-worksheet.md), code và raw/log/JUnit đề tài mới trong `evidence/lost-found/` local. Yêu cầu công bố áp dụng nhánh cá nhân `HoangBaoNguyen`; `main` và bản nhóm/demo cũ chưa tự động được đổi theo candidate này.

## 6. Kết quả sửa và phạm vi tự thực hiện

Các thao tác đọc nguồn, viết/sửa code, chạy test và gọi API do trợ lý thực hiện trong workspace theo yêu cầu người học. Người học chưa phỏng vấn operator hay đo ROI. Cần tự đọc/hiểu cả hai phần để bảo vệ; không nhận trợ lý chạy test là nghiên cứu thực địa của người học hoặc của nhóm.
