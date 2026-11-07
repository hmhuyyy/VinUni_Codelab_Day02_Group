# Bài cá nhân - Hoàng Bảo Nguyên / 2A202603384

Nhánh nộp: `HoangBaoNguyen`. Các file bài làm:

- [01-problem-scan.md](01-problem-scan.md): 5 problems và 3 Quick Cards.
- [02-deep-dive-report.md](02-deep-dive-report.md): phân tích, quyết định và kết quả thử nghiệm/đầu ra model.
- [03-ai-log.md](03-ai-log.md): nhật ký sử dụng và phản biện AI.
- [04-workflow-diagram.pdf](04-workflow-diagram.pdf): workflow trước/sau.
- [05-one-page-artifact-pack.pdf](05-one-page-artifact-pack.pdf): bản tóm tắt một trang theo slide.
- [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py): prototype Python cá nhân.

Chạy prototype trên Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:GEMINI_API_KEY="YOUR_API_KEY"
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py
```

Code mặc định dùng `gemini-2.5-flash` theo worksheet. Lượt xác nhận được ghi trong báo cáo dùng `gemini-3.5-flash-lite` do giới hạn quota/khả dụng của tài khoản; để chủ động chọn model, đặt `$env:GEMINI_MODEL="gemini-3.5-flash-lite"` trước khi chạy. Không đưa key thật vào code hoặc Git.

Kết quả đã ghi nhận: 82 tests offline đạt; ba ca lõi chạy thật đạt 3/3; bộ chấm kỹ thuật gốc đạt 10/10. Các số liệu kinh doanh là giả định có nhãn. Log chi tiết và công cụ soạn tài liệu được giữ local; kết quả cần chấm nằm trong báo cáo.

Kiểm tra bộ bài trước khi nộp:

```powershell
.\.venv\Scripts\python.exe autograder/autograder.py --section-a
# Chấm cả code: cần API key/model có quota
.\.venv\Scripts\python.exe autograder/autograder.py
```

Code `.py` nằm trên nhánh cá nhân; trưởng nhóm chọn báo cáo đưa vào `main` và đại diện nộp form theo hướng dẫn lớp.

Đề và tài liệu tham khảo được giữ ở nhánh `main`: [hướng dẫn lớp](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/main/README.md), [worksheet](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/main/01-worksheet.md), [bài mẫu](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/main/02-deliverable-example.md), [gợi ý đề tài](https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/blob/main/03-inspiration-kit.md).
