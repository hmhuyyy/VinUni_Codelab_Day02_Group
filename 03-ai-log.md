# AI Log & Reflection — đổi sang đề tài độc lập

**Học viên:** Hoàng Bảo Nguyên / **MSSV:** 2A202603384
**Ngày:** 08/11/2026 / **Nhánh cá nhân:** `HoangBaoNguyen`
**Đề tài:** Vinpearl Lost-Property Intake — chuẩn hoá phiếu đồ nhặt được.


## 1. Yêu cầu có thật và phạm vi AI tham gia

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
| Yêu cầu mới của người học: giữ Vinpearl và sửa check | Đổi gate prompt sang chỉ thị + 10 negative probes, giữ trọng số và các gate còn lại | Lượt thật đạt 10/10 exit 0; 30 test grader và tổng 122 offline đạt; ghi rõ grader đã điều chỉnh |

## 3. Những lỗi/giới hạn AI đã phải sửa

### 3.1 Chọn đề tài quá sát bài mẫu

Đề tài trước là mở rộng kỹ thuật cho cùng bài toán Xanh SM. Người học phát hiện và yêu cầu đổi. Cách sửa là xây một candidate khác về nghiệp vụ, actor, nguồn dữ liệu, output và quyền hạn; các kết quả 82 tests/3 raw của bài trước không được dùng cho đề tài mới. Đây là điểm trợ lý cần làm rõ sớm hơn khi tư vấn tính độc lập.

### 3.2 Response model thật bỏ dấu ngoặc tag

Lượt `live-flash-probe.json`, prompt LF-1, Gemini 2.5 Flash trả dòng đầu `DRAFT_ONLY`, thiếu `[` và `]`. Validator chặn đúng; không thêm tag vào raw rồi tính pass. Prompt LF-2 ghi rõ 12 ký tự ASCII và dấu ngoặc literal; thêm regression về bare tag. Hai response LF-2 trên 2.5 Flash đạt trong lượt core, nhưng một case trả 429; lần thử riêng còn 429. Giữ tất cả các lượt thay vì che kết quả bất lợi.

### 3.3 Source quote không chứng minh đúng vai trò field

Regression đặt một đoạn location có thật vào `item_description`: contract source-only vẫn có thể qua. Annotation fixture độc lập phát hiện sai; ngoài tập fixture phải do reviewer nghiệp vụ kiểm. Vì vậy không nói source anchoring bảo đảm mọi dữ kiện/ngữ nghĩa đúng hoặc xác nhận món đồ thuộc ai.

### 3.4 Template có thể đủ

Baseline parse nhãn và một mẫu câu tự do đã đạt 12/12 fixture. Tập test còn nhỏ/quen thuộc, chưa có người đo công sửa; chưa chứng minh giá trị LLM vượt form/rule. LLM chỉ là feature thử nghiệm; nếu form đáp ứng tốt thì bỏ LLM.

### 3.5 Sửa check gắn với worked example theo yêu cầu mới

Lượt đầu dùng grader nguyên bản và ghi nhận 9,50/10. Sau đó người học yêu cầu giữ Vinpearl Lost-Property Intake, thay check keyword của ví dụ và sửa để đạt 10/10. Trợ lý đã điều chỉnh chính file grader trong nhánh cá nhân; không thêm keyword pin/xe sạc vào System Prompt, không sửa log cũ và không nhận thay đổi này do giảng viên ban hành.

Check mới vẫn cần chỉ thị rõ và validator hoạt động: phải nhận reference đúng, chặn 10 response sai bằng lỗi BoundaryViolation có kiểm soát. Bổ sung 30 test grader, gồm validator bị làm yếu/luôn nhận/luôn từ chối hoặc crash. Kết quả thật của grader điều chỉnh là 10,00/10, exit 0; các test offline tổng 122/122 đạt. Script tiếp tục gọi Gemini thật trong full run. Model được chọn tường minh là 3.5 Flash-Lite; điều kiện 2.5 Flash trong worksheet vẫn cần được xử lý riêng như báo cáo.

Giới hạn cần hiểu: điều chỉnh công cụ kiểm kỹ thuật không tạo thêm dữ liệu business, không chứng minh chất lượng với operator và không tự quyết định điểm chính thức. Log/phạm vi chấm được ghi rõ để người học và người chấm kiểm lại.

## 4. Prompt và dữ liệu có dấu vết

System prompt thực trong code: `LF-2-literal-draft-envelope`. User input và application_context được gửi riêng bằng JSON; expected_fields của fixture không gửi cho model. Ba core attacks là ép trả đồ/đóng hồ sơ, tự điền nơi nhặt thiếu và giả admin bỏ nhãn/duyệt. Ca mở rộng kiểm unknown time, context thiếu, mâu thuẫn, note injection, đổi id, PII và câu tự do.

Synthetic notes/annotations do trợ lý tạo để kiểm code, không phải field research hoặc log khách sạn. Chưa được SME xác nhận. Không gửi dữ liệu khách thật hoặc key vào báo cáo/Git. Ba raw core model cuối ở mục 10.2 của Deep-Dive; model/thời điểm/phiên bản ghi rõ theo từng lượt.

## 5. Reflection để người học tự kiểm trước khi bảo vệ

Điểm cần hiểu là sự khác nhau giữa có câu nguồn và đúng vai trò ngữ nghĩa, giữa phiếu nháp đủ trường và quyền trả tài sản, giữa template/fixture với response model, giữa số đo kỹ thuật và hiệu quả vận hành. Cần giải thích được `build_rule_template`, `validate_response`, `safe_fallback`, `evaluate_prompt` và vì sao API lỗi không phải hallucination.

Tôi chưa phỏng vấn operator, chưa có baseline hay ROI. Việc cần tiếp theo là kiểm pain/workflow với người có quyền, chốt dữ liệu/rubric/cỡ mẫu và so phương án bằng công sửa thực. Không dùng AI đoán số để làm đủ bảng. Nội dung reflection này được AI hỗ trợ biên tập; người học cần đọc, sửa theo hiểu biết thật và không nhận đã làm những hoạt động chưa diễn ra.

## Nguồn và trạng thái bàn giao

[Nguồn nghiệp vụ S1](https://careers.vinpearl.com/job/vinpearl-nha-trang-truong-bo-phan-tien-sanh-4416), [worksheet](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/9ad1a44e43eb21162229831bad6c38dfc69ade0d/01-worksheet.md), code và raw/log/JUnit đề tài mới trong `evidence/lost-found/` local. Yêu cầu công bố áp dụng nhánh cá nhân `HoangBaoNguyen`; `main` và bản nhóm/demo cũ chưa tự động được đổi theo candidate này.
