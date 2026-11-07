# Kiểm chứng phiên bản sẵn sàng nộp

**Hoàng Bảo Nguyên / 2A202603384 / HoangBaoNguyen**

Thời điểm kiểm chứng: 2026-11-07T22:08:36+07:00 (UTC+07).

## Kết quả phiên bản hiện tại

| Hạng mục | Kết quả | Evidence |
|---|---|---|
| Test offline | **82/82**, không có failure/error | `offline-tests-submission.xml` |
| Bộ chấm gốc | **10/10**, script exit 0 | `autograder-submission.txt` |
| Live core | **3/3 raw responses đạt validator v3**, 0 case API error | `live-results.json` |
| Model / prompt / validator | `gemini-3.5-flash-lite` / `2-semantic-commitment-guard` / `3-audit-regressions` | JSON live và metadata |
| Đối chứng template | 3/3 template và 3/3 LLM qua contract trên cùng ba context, action trùng 3/3 | `template-comparison.md`, `.json` |
| Workflow PDF | Hai trang; giữ bản đã được kiểm tra | `../04-workflow-diagram.pdf` |
| Artifact pack PDF | **Đúng một trang A4**, đã render/kiểm tra trực quan | `../05-one-page-artifact-pack.pdf` |
| Quick Cards | Ba card, mỗi card 3-5 bước; Card #1 đã gộp bước cuối | `../01-problem-scan.md` |
| Tài liệu lớp / autograder | Giữ nguyên | Git diff với template |

Đây là kiểm chứng kỹ thuật và độ đầy đủ của bài cá nhân, không phải điểm chính thức hoặc xác nhận đã hoàn thành bài nhóm.

## Các điểm audit đã xử lý

- Kiểm khoảng số trước `math.isfinite`, số pin/tuổi dữ liệu/khoảng cách cực lớn không còn làm policy/fallback overflow.
- Bổ sung regression cho câu “đã được điều động”, hướng dẫn lái xe trái nhánh và id trạm mô phỏng ngoài context. Validator vẫn là bộ lọc bảo thủ, không chứng minh mọi ngữ nghĩa đúng.
- Thêm 19 tests so với snapshot 63 tests; raw history giữ riêng, không sửa output model cũ.
- Có baseline template thực thi được và đối chứng trên output model thật đã ghi, không dùng mock làm bằng chứng model.
- Cụ thể hóa Q1-Q4, ngưỡng “sửa nhẹ” và điều kiện LLM hơn template. Đây là gate đề xuất, chưa có reviewer nghiệp vụ chấm.
- AI Log bổ sung câu hỏi thật của người học, phản biện yêu cầu model, kết quả audit và sửa code; không nhận hoạt động field research chưa xảy ra.

## Điều kiện model và giới hạn

Code giữ default `gemini-2.5-flash` theo worksheet. Snapshot v1 đã có 3/3 core trên Flash; sau đó quota ngày của model này bị chặn. Bản xác nhận hiện tại dùng `gemini-3.5-flash-lite` theo cấu hình tường minh; không nhận là kết quả cùng model. Prompt v2 được giữ nguyên; validator v3 được ghi riêng.

Bộ khai báo có chín adversarial cases; lượt hiện tại xác nhận ba ca lõi, đáp ứng mức tối thiểu ba trong worksheet. Không tuyên bố cả chín ca trên model cuối đều đã đạt. `semantic_human_review=not_performed` vẫn đúng.

Đối chứng ba case chỉ kiểm contract/action; không đo độ hài lòng, thời gian sửa của operator hoặc ROI. Kết luận vẫn **GO technical synthetic; NOT YET pilot thật**. Những số liệu 12 phút, volume và chi phí là giả định có nhãn. Không cần dựng thêm hoạt động phỏng vấn để làm bài có vẻ hoàn chỉnh.

## Cách nộp

Bộ bài cá nhân được chuẩn bị cho nhánh `HoangBaoNguyen`; xem `../SUBMISSION_CHECKLIST.md` và hướng dẫn `../00-submission-guide.md`. Key không nằm trong source, evidence hoặc ZIP. Trưởng nhóm vẫn cần review/chọn báo cáo đưa vào main và đại diện điền form; code cá nhân giữ ở nhánh riêng.

Audit Sol 6.1 trước đó chấm 91/100 tại snapshot `bb1f3bd`; đó không tự động là điểm của phiên bản đã sửa. Không thay đổi hay nâng điểm audit bằng suy đoán.
