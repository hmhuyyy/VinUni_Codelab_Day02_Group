# Checklist nộp bài cá nhân - Hoàng Bảo Nguyên / 2A202603384

## Bộ bài trên nhánh HoangBaoNguyen

- [x] `01-problem-scan.md`: 5 problems, đủ 4 lenses; 3 Quick Cards, mỗi card 3-5 bước, metric và boundary.
- [x] `02-deep-dive-report.md`: workflow, Problem Statement 6 trường, AI Fit, HITL/fallback, Readiness, quyết định và next experiment.
- [x] `03-ai-log.md`: hỗ trợ/sai/sửa của AI, câu hỏi có thật của người học, lỗi audit và cách sửa; không nhận đã khảo sát thực địa.
- [x] `04-workflow-diagram.pdf`: current/future-state, hai trang có thời gian/handoff/bottleneck.
- [x] `05-one-page-artifact-pack.pdf`: bản một trang có Problem Statement, RACI-lite, Readiness, quyết định và next experiment theo slide.
- [x] `starter-code/prompt_prototype.py`: SDK Gemini thật, JSON contract, nhãn nháp, 9 ca khai báo và 3 ca lõi chạy mặc định.
- [x] Code/guard đã sửa lỗi overflow và phản ví dụ audit; tests và raw evidence được tách rõ.
- [x] `evidence/template-comparison.md`: đối chứng nhỏ với output model đã ghi, không dựng kết quả người dùng.
- [x] Model mặc định theo đề; model chạy thay thế và giới hạn quota được ghi rõ, không đánh đồng hai model.
- [x] Key nằm trong `.env` bị Git bỏ qua; gói bàn giao không chứa key hoặc môi trường ảo.

Đọc kết quả hiện hành tại `evidence/submission-verification.md`. Các file verification/environment cũ là snapshot lịch sử; audit 91/100 tại `bb1f3bd` không tự biến thành điểm của phiên bản mới.

## Trước khi bạn trình bày

- Đọc `05-one-page-artifact-pack.pdf` và `06-defense-notes.md`; tự giải thích được actor, bottleneck, Rule vs LLM, fallback và NOT YET.
- Giữ các giả định đúng nhãn. Nếu bạn có trải nghiệm hoặc dữ liệu thật, bổ sung nguồn và sửa reflection theo điều thực sự diễn ra.
- Nếu người chấm muốn chạy lại, cấu hình key có quota và model phù hợp; không cần cung cấp key cá nhân công khai.

## Việc của quy trình nhóm

- [ ] Nhóm review các candidate và thống nhất bộ báo cáo chung.
- [ ] Trưởng nhóm chọn/tổng hợp `.md` và sơ đồ lên `main`; không merge code `.py` cá nhân vào `main`.
- [ ] Duy nhất trưởng nhóm điền form nộp repo chung theo README lớp.

Ba việc cuối là bước nộp chung của nhóm, không được khai là đã hoàn thành bằng việc cá nhân push nhánh riêng. Link nhánh bài cá nhân: https://github.com/hmhuyyy/VinUni_Codelab_Day02_Group/tree/HoangBaoNguyen
