# Day02 — Vinpearl Lost-Property Intake

**Học viên:** Hoàng Bảo Nguyên / **MSSV:** 2A202603384
**Ngày:** 08/11/2026 / **Nhánh cá nhân:** `HoangBaoNguyen`
**Đề tài:** Vinpearl Lost-Property Intake — chuẩn hoá phiếu đồ nhặt được.


Bài cá nhân mới thay thế đề tài điều phối sự cố pin. Phạm vi: đọc ghi chú đồ nhặt được, tạo phiếu nháp ba trường có trích dẫn, chỉ ra thông tin thiếu/mâu thuẫn để lễ tân kiểm tra. Prototype không xác nhận chủ sở hữu, trả đồ, gửi tin hoặc ghi hệ thống thật.

| File | Nội dung |
|---|---|
| [01-problem-scan.md](01-problem-scan.md) | Năm cơ hội mới, ba Quick Cards, lựa chọn có căn cứ |
| [02-deep-dive-report.md](02-deep-dive-report.md) | Workflow, PS sáu trường, AI Fit, metric thực đo, raw outputs và Decision |
| [03-ai-log.md](03-ai-log.md) | Nhật ký giúp/sai/sửa/kiểm, lỗi tag và quota thực sự đã gặp |
| [04-workflow-diagram.pdf](04-workflow-diagram.pdf) | Current/Future-state, handoff, thời gian chưa đo, HITL và fallback |
| [05-one-page-artifact-pack.pdf](05-one-page-artifact-pack.pdf) | Một trang PS, RACI-lite, Readiness, Decision và next experiment |
| [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) | SDK Gemini, contract, source-evidence validator, template và 12 adversarial fixtures |

## Chạy

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
# Offline: không cần key hoặc gọi model
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --mode template --limit 12
# LIVE: key đặt trong .env local, hoặc biến môi trường GEMINI_API_KEY
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --mode live --model gemini-2.5-flash --limit 3
```

Default là **live / Gemini 2.5 Flash** theo worksheet. `--mode template` là baseline xác định, không phải Gemini. `--model` hoặc biến môi trường `GEMINI_MODEL` chọn model tường minh; `.env` chỉ nạp key, không kế thừa model của đề tài cũ. Không đưa key vào code/Git. SDK được pin trong `requirements.txt`.

## Kết quả và giới hạn

- **92/92 test offline** của đề tài mới đạt; không tái sử dụng số 82 của đề tài cũ.
- **12/12 fixture template** qua contract và khớp annotation do trợ lý soạn cho dữ liệu synthetic.
- Lượt core cuối: **3/3 raw Gemini 3.5 Flash-Lite** qua contract và khớp annotation; UTC `2026-11-08T03:16:47.298345+00:00`. Raw nằm ngay trong Deep-Dive.
- Gemini 2.5 Flash có response thật; LF-1 thiếu dấu ngoặc ở tag. LF-2 có hai response core đạt và các lượt HTTP 429. Không nhận kết quả Lite là đã hoàn tất ba ca cuối trên 2.5 Flash. Xem bảng tất cả lượt ở báo cáo.
- **Grader đã điều chỉnh: 10,00/10; exit 0.** Thay check keyword pin bằng kiểm chỉ thị và 10 response vi phạm độc lập (tag, source, approval, schema, action). Giữ trọng số và bốn check code còn lại. Grader gốc từng trả 9,50/10; log cũ giữ nguyên. Đây là điểm kỹ thuật từ grader được điều chỉnh trong repo, không tự nhận là điểm chính thức của giảng viên.
- **122/122 test offline đạt:** 92 test prototype + 30 test grader. Bộ test grader kiểm cả validator bị làm yếu, luôn nhận, luôn từ chối và crash; không chỉ kiểm happy path.
- Thời gian vận hành, volume, acceptance của lễ tân và ROI **chưa đo/chưa tính**. Không dùng AI dự đoán số liệu. Chưa có reviewer nghiệp vụ xác nhận annotation hoặc workflow.

```powershell
# Chỉ kiểm sự tồn tại file, không gọi API
.\.venv\Scripts\python.exe autograder/autograder.py --section-a
# Lặp lại lượt 10/10: chọn model đã dùng tường minh; full grader gọi API thật
$env:GEMINI_MODEL="gemini-3.5-flash-lite"
.\.venv\Scripts\python.exe autograder/autograder.py
Remove-Item Env:\GEMINI_MODEL
```

Tests, log/JUnit và công cụ tạo PDF giữ local theo yêu cầu gói nộp gọn. Ba raw responses và thông tin nguồn được nhúng trong báo cáo để reviewer đối chiếu. Nhánh cá nhân chứa code; không đưa code cá nhân vào main. Bản nhóm/demo Xanh SM đã soạn trước đây là đề tài cũ, chưa tự động đổi theo bài cá nhân này.

Nguồn nghiệp vụ: [Vinpearl — mô tả công việc Trưởng Bộ phận Tiền sảnh](https://careers.vinpearl.com/job/vinpearl-nha-trang-truong-bo-phan-tien-sanh-4416), có nhiệm vụ xử lý đồ thất lạc/nhặt được; nguồn công khai này không cung cấp SOP, thời gian, volume hoặc quyền truy cập nội bộ. [Worksheet lớp](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/9ad1a44e43eb21162229831bad6c38dfc69ade0d/01-worksheet.md) là nguồn rubric/định dạng. Bài này chưa được doanh nghiệp khảo sát hoặc phê duyệt.
