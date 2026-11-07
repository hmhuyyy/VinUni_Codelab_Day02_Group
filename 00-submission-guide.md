# Bộ bài cá nhân - Hoàng Bảo Nguyên

**Mã học viên:** 2A202603384 | **Nhánh:** `HoangBaoNguyen` | **Ngày:** 07/11/2026

**Đề tài:** Xanh SM - chuẩn hóa thông tin sự cố pin và soạn nháp đề xuất xử lý cho điều phối viên.

## 1. Đọc và trình bày theo thứ tự

1. `01-problem-scan.md`: năm cơ hội, ba cards và lý do chọn một candidate.
2. `02-deep-dive-report.md`: workflow, Problem Statement, baseline, AI Fit, RACI và gate.
3. `04-workflow-diagram.pdf`: hai trang current-state/future-state, thời gian và handoff.
4. `starter-code/prompt_prototype.py`: code cá nhân và chín ca tấn công.
5. `03-ai-log.md`: lịch sử hỗ trợ AI, lỗi thật và cách sửa.
6. `evidence/verification-summary.md`: kết quả thực thi cuối và giới hạn.

Tên/mã học viên được dùng để nhận diện bài. Bối cảnh doanh nghiệp và các metric kinh doanh là giả định discovery; không có khảo sát hoặc dữ liệu nội bộ thật.

## 2. Ánh xạ với rubric

| Gate | Điểm | Phần bài trả lời |
|---|---:|---|
| I1 Scan & Cards | 15 cá nhân | `01-problem-scan.md`: 5 problems, đủ 4 lenses, 3 cards, hội tụ và phản biện |
| I2 Prototyping | 10 cá nhân | Python gọi Gemini thật, raw output, 3 core + 6 extended cases; offline tests riêng |
| I3 AI Log | 15 cá nhân | `03-ai-log.md`: yêu cầu đã có, lỗi giả định/cấu hình/quota, điều chỉnh và reflection |
| G1 Workflow | 20 nhóm | Báo cáo mục 2 và sơ đồ: 6 bước, actor, input/output, handoff, thời gian, nhánh thiếu dữ liệu |
| G2 Problem Statement | 20 nhóm | Báo cáo mục 3-4: 6 fields, metric và kế hoạch eval |
| G3 AI Fit | 10 nhóm | Báo cáo mục 5-6: Rule vs LLM vs Agent, flow có HITL/fallback |
| G4 Decision | 10 nhóm | Báo cáo mục 8-9: tính fallback, readiness, NOT YET pilot và next experiment |

Các mục G1-G4 là đề xuất đóng góp của cá nhân, chưa mặc định thành bài nhóm hoặc được trưởng nhóm chấp nhận. Điểm nội dung do giảng viên đánh giá.

## 3. Chạy trên Windows PowerShell

Mở terminal ở thư mục repository. Gọi Python của môi trường ảo trực tiếp để không phụ thuộc activation policy.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Nếu `.venv` đã có thì dùng luôn, không cần tạo lại. `.env` ở máy hiện tại đã được cấu hình và Git bỏ qua; khi sang máy khác copy `.env.example` thành `.env`, điền key local. Không đưa key vào code, log, commit hoặc file zip.

```powershell
# Offline: không gọi Gemini, không tính là model pass
.\.venv\Scripts\python.exe -m pytest -q --junitxml=evidence/offline-tests.xml

# Live: mặc định 3 ca lõi chạy song song, có sử dụng quota API
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --report evidence/live-user-run.json

# Live mở rộng: 9 ca, giãn request khi quota thấp
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --limit 9 --pace-seconds 20 --report evidence/live-user-extended.json

# Bộ chấm gốc: Section A không gọi API
.\.venv\Scripts\python.exe autograder/autograder.py --section-a

# Full grader có chạy prototype thật một lần
.\.venv\Scripts\python.exe autograder/autograder.py
```

Mặc định model `gemini-2.5-flash` theo lab, SDK cấu hình `v1beta`, timeout 11 giây và tối đa 2 attempts chỉ cho lỗi server 500/502/503/504; không tự retry 400/404/429. Ba ca lõi chạy song song để phù hợp timeout 30 giây của grader. Nếu model không còn khả dụng, kiểm tra rồi ghi rõ `GEMINI_MODEL` trong `.env`; không tự đổi model để so kết quả như cùng điều kiện.

**Điều kiện trên máy hiện tại:** key đã chạm quota 20 requests/ngày của Flash. Model 2.5 Flash-Lite trả 404 cho tài khoản mới; theo chỉ định API, `.env` chọn `GEMINI_MODEL=gemini-3.5-flash-lite` cho lượt kiểm tra bổ sung. Evidence ghi đúng model. Muốn chạy đúng Flash theo đề, đổi biến này về `gemini-2.5-flash` khi quota hồi phục. `.env` không nằm trong bài/ZIP; máy khác sẽ dùng model default nếu chưa cấu hình override.

Không chạy nhiều lệnh live liên tiếp khi quota thấp. HTTP 429 là lỗi dịch vụ; quota ngày cần đợi reset hoặc dùng cấu hình model/tài khoản phù hợp, không chỉ nghỉ vài giây. Không dùng output mẫu để làm bộ chấm qua. CLI trả 0 khi mọi raw response được chọn đều đạt contract, 1 khi có lỗi và 2 khi thiếu key. Fallback không làm một raw failure thành pass.

`[DRAFT_ONLY]` + newline + JSON là giao thức text; validator Python kiểm tra JSON và policy. Structured response được quy định bằng hợp đồng và parser, không tuyên bố API ép JSON schema khi prefix làm output không phải JSON thuần.

## 4. Tái tạo sơ đồ

```powershell
.\.venv\Scripts\python.exe tools/build_workflow_pdf.py
```

Đầu ra là PDF hai trang ở root để bộ chấm nhận đúng tên. Cần font Arial của Windows hoặc biến `LAB_FONT_DIR` trỏ tới thư mục có `arial.ttf` và `arialbd.ttf`.

## 5. Bàn giao và nộp cá nhân

- Làm trên `HoangBaoNguyen`; kiểm tra `git status` và `git diff` trước commit.
- Giữ file `.py` cá nhân ở nhánh cá nhân. Trưởng nhóm chọn báo cáo/sơ đồ phù hợp để đưa vào `main` theo README của lớp.
- Nhật ký và các con số giả định cần được người học đọc, hiểu và xác nhận trước khi nộp.
- Không có tuyên bố đã họp nhóm, phỏng vấn hoặc triển khai thực địa.

Khi đã review nội dung và muốn nộp lên GitHub, thực hiện trong nhánh cá nhân:

```powershell
git status
git add 00-submission-guide.md 01-problem-scan.md 02-deep-dive-report.md 03-ai-log.md 04-workflow-diagram.pdf
git add starter-code/prompt_prototype.py tests tools evidence requirements.txt .gitignore .env.example
git commit -m "Complete Day02 individual lab - Hoang Bao Nguyen 2A202603384"
git push -u origin HoangBaoNguyen
```

Các lệnh commit/push trên là hướng dẫn cho bước nộp; quá trình chuẩn bị bộ bài không tự push hoặc thay đổi main.

## 6. Tài liệu kỹ thuật

- [Google Gen AI Python SDK](https://googleapis.github.io/python-genai/): client, system instruction, HTTP options và timeout.
- `README.md`, `01-worksheet.md`: yêu cầu lớp và quy tắc chấm/nộp.
- PDF bài giảng được người học cung cấp: khung Problem Statement, RACI, readiness và next experiment. PDF gốc được giữ ở máy người học, không chép toàn bộ tài liệu giảng dạy vào bài cá nhân.
