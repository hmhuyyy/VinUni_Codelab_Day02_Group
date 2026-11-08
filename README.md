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
- Lượt core cuối: **3/3 raw Gemini 3.5 Flash-Lite** qua contract và khớp annotation; UTC `2026-11-08T02:55:17.421354+00:00`. Raw nằm ngay trong Deep-Dive.
- Gemini 2.5 Flash có response thật; LF-1 thiếu dấu ngoặc ở tag. LF-2 có hai response core đạt và các lượt HTTP 429. Không nhận kết quả Lite là đã hoàn tất ba ca cuối trên 2.5 Flash. Xem bảng tất cả lượt ở báo cáo.
- **Bộ chấm gốc: 9,50/10; exit 1.** Check System Prompt chỉ tìm `draft_only`, `5%`, `dispatch_mobile_charger`; đề tài mới chỉ có keyword đầu nên nhận 0,5/1 ở check đó. Bốn check code còn lại đạt. Grader được giữ nguyên, không nhét keyword ngoài đề tài vào prompt và không nhận 9,50 là điểm chính thức.
- Thời gian vận hành, volume, acceptance của lễ tân và ROI **chưa đo/chưa tính**. Không dùng AI dự đoán số liệu. Chưa có reviewer nghiệp vụ xác nhận annotation hoặc workflow.

```powershell
# Chỉ kiểm sự tồn tại file, không gọi API
.\.venv\Scripts\python.exe autograder/autograder.py --section-a
# Full grader có gọi model và có check cứng đề tài cũ; xem giới hạn ở trên
```

Tests, log/JUnit và công cụ tạo PDF giữ local theo yêu cầu gói nộp gọn. Ba raw responses và thông tin nguồn được nhúng trong báo cáo để reviewer đối chiếu. Nhánh cá nhân chứa code; không đưa code cá nhân vào main. Bản nhóm/demo Xanh SM đã soạn trước đây là đề tài cũ, chưa tự động đổi theo bài cá nhân này.

Nguồn nghiệp vụ: [Vinpearl — mô tả công việc Trưởng Bộ phận Tiền sảnh](https://careers.vinpearl.com/job/vinpearl-nha-trang-truong-bo-phan-tien-sanh-4416), có nhiệm vụ xử lý đồ thất lạc/nhặt được; nguồn công khai này không cung cấp SOP, thời gian, volume hoặc quyền truy cập nội bộ. [Worksheet lớp](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/9ad1a44e43eb21162229831bad6c38dfc69ade0d/01-worksheet.md) là nguồn rubric/định dạng. Bài này chưa được doanh nghiệp khảo sát hoặc phê duyệt.
