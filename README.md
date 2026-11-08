# Day02 — Hoàng Bảo Nguyên / 2A202603384

**Nhánh cá nhân:** `HoangBaoNguyen` · **Cập nhật:** 08/11/2026.

## Phân biệt hai phần bài

| Phần | Nội dung | File / căn cứ |
|---|---|---|
| Business Deep-Dive | **Vinpearl Lost-Property Intake**: phiếu đồ nhặt được, evidence, thông tin thiếu, người duyệt | Ba báo cáo Markdown và hai PDF bên dưới |
| Code được giao của lớp (I2) | **Battery-dispatch boundary lab** theo starter: `[DRAFT_ONLY]`, pin <5%, trạm >5 km, `dispatch_mobile_charger` | `starter-code/prompt_prototype.py` |
| Bộ chấm | **Nguyên trạng bản lớp**, khớp byte với commit template `9ad1a44` | `autograder/autograder.py` |

Đề tài phân tích khác ví dụ mẫu; bài code cố định vẫn làm đúng yêu cầu starter. Thử nghiệm Vinpearl trước đây là bằng chứng phụ trợ cho nghiên cứu business, không thay bài code I2. Không dùng grader đã sửa để báo điểm hiện tại.

- [01-problem-scan.md](01-problem-scan.md): 5 problems / 4 lenses / 3 cards về business.
- [02-deep-dive-report.md](02-deep-dive-report.md): G1-G4 Vinpearl, tách bằng chứng phụ trợ ở mục 10 và code lớp ở mục 11.
- [03-ai-log.md](03-ai-log.md): giúp/sai/sửa/kiểm, bao gồm việc khôi phục grader sau đối chiếu.
- [04-workflow-diagram.pdf](04-workflow-diagram.pdf): workflow business Vinpearl.
- [05-one-page-artifact-pack.pdf](05-one-page-artifact-pack.pdf): PS/RACI/Readiness/Decision cho Vinpearl, ghi rõ kết quả code riêng.
- [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py): code cố định cần chấm.

## Chạy bài code và bộ chấm nguyên bản

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
# Đặt GEMINI_API_KEY trong .env local hoặc biến môi trường, không đưa lên Git.
$env:GEMINI_MODEL="gemini-2.5-flash"
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py
.\.venv\Scripts\python.exe autograder/autograder.py
```

**Kết quả kiểm tra thật của bản sửa:** grader gốc **10,00/10, exit 0**; Code-1 khớp cả ba keyword, SDK/tests/execution/assertions đều đạt. Ba raw responses mới của bài code qua validator, nguồn `evidence/required-code/live-results.json`, UTC `2026-11-08T03:41:10.490562+00:00`. Log chấm gốc: `evidence/required-code/original-grader-final.txt`; raw output đã nhúng ở Deep-Dive mục 11.

**Điều kiện model:** lượt 10/10 trên dùng `gemini-3.5-flash-lite` được chọn tường minh. Thử 2.5 Flash hiện trả HTTP 429 và không có raw response; không nhận kết quả thay thế là 2.5 Flash. Code giữ default 2.5 Flash theo worksheet. Khi có quota, chạy lại đúng model; không tự nhận giảng viên chấp thuận thay thế.

Để tái lập đúng cấu hình của lượt đã ghi (key có quota):

```powershell
$env:GEMINI_MODEL="gemini-3.5-flash-lite"
.\.venv\Scripts\python.exe autograder/autograder.py
Remove-Item Env:\GEMINI_MODEL
```

Script hiển thị model thực dùng; đọc key/model từ môi trường hoặc `.env` local. **Không có key thì phải báo BLOCKED/exit 2**; kiểm Code-4/5 khi không có key không thể chứng minh thực thi API thành công. Không tự chuyển sang mock hoặc in pass giả. Kiểm file không gọi API: `python autograder/autograder.py --section-a`.

## Bằng chứng tách biệt

- **Bài code lớp:** 9 adversarial cases khai báo, mặc định 3 core; 82/82 offline tests đạt; core mới 3/3 raw qua validator.
- **Business Vinpearl phụ trợ:** 12/12 template fixture, 92/92 test phụ trợ và 3/3 raw core lịch sử trên 3.5 Flash-Lite. Đây không phải kết quả I2 hiện tại, không phải operator review hoặc business ROI.
- **Tổng test hiện hành:** 174/174 = 82 code lớp + 92 phụ trợ. Test grader tự sửa trước đó đã lưu lịch sử, không dùng để chấm bài hiện tại.
- **Integrity:** grader đã khôi phục, Git blob `65fe932ffba25b19b17efa73293b5fae9b6a7175`, trùng bản template. Kết quả 10/10 từ grader tự điều chỉnh trước đây không dùng làm điểm hiện tại.
- Thời gian, volume, acceptance vận hành và ROI của Vinpearl chưa đo/chưa tính; không dùng AI dự đoán số liệu.

Log/JUnit và công cụ phụ trợ giữ local theo yêu cầu gói nộp gọn. [Mã thử nghiệm Vinpearl lịch sử](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/523099259cd1c1351bd5f4e7acf2ca5fdf0c0c13/starter-code/prompt_prototype.py) vẫn truy cập được trong Git; code được chấm hiện tại là file starter-code ở nhánh này. Code cá nhân không merge vào main; báo cáo nhóm là phần riêng. Hướng dẫn/rubric gốc ở [commit template](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/9ad1a44e43eb21162229831bad6c38dfc69ade0d/README.md).
