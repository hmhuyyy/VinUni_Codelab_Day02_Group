# Audit độc lập Sol 6.1 — Day02 Hoàng Bảo Nguyên / 2A202603384

**Điểm trung tâm: 91/100 = cá nhân 36/40 + chất lượng nội dung nhóm 55/60. Khoảng chấm hợp lý: 87–95/100.** Autograder **10/10** là kết quả kỹ thuật riêng, không có nghĩa điểm nội dung 100.

Snapshot: `bb1f3bd0dd7366380dca8212cf2e6b48857dff22`, nhánh `HoangBaoNguyen`, đã push và local/remote SHA trùng theo kiểm chứng của agent chính. G1–G4 chấm candidate này nếu đưa vào bài nhóm; **không trừ vì chưa push, chưa merge main, chưa họp hoặc chưa điền form**.

Đã đối chiếu README, worksheet, worked example/inspiration, ba báo cáo, code/tests và evidence chính. Render/quan sát đủ hai trang PDF: rõ chữ, đủ handoff, thời gian, bottleneck và ngoại lệ. Chạy lại offline: **63 passed in 0.58s**; thêm hai probe dưới đây. Không gọi API/đọc `.env` hoặc key; không sửa bài/evidence. Workingtree vẫn sạch. Rubric gốc: `01-worksheet.md:24–37`.

## Điểm và căn cứ

| Gate | Điểm | Đánh giá |
|---|---:|---|
| **I1 Scan & Cards** | **14/15** | Đủ 5 problems, 4 lenses và 3 card có actor/workflow/metric/boundary; có phản biện Rule. `01-problem-scan.md:13–63`. Trừ nhẹ chất lượng đánh giá card phụ: ngưỡng và ranking chưa có mẫu dữ liệu hoặc lý giải cụ thể cho từng điểm số (`43–49`, `57–75`). Không bắt buộc phải phỏng vấn để làm lab. |
| **I2 Prototyping** | **9/10** | SDK thật, raw response, ít nhất 3 adversarial prompts, validator/fallback tách bạch; 63 tests pass. `starter-code/prompt_prototype.py:120–201`, `212–277`. V1 có 3/3 trên đúng 2.5 Flash; V2 cuối có 3/3 trên 3.5 Flash-Lite (`evidence/live-results.json:6–26`). Chưa xác nhận prompt cuối trên đúng model đề; guard còn giới hạn và có overflow nhỏ tái hiện dưới đây. **Không trừ vì chưa chạy đủ 9 ca:** đề chỉ yêu cầu ≥3. |
| **I3 AI Log & Reflection** | **13/15** | Có giúp/sai/sửa, lỗi SDK/quota thật và semantic overclaim dẫn tới v2/regression. `03-ai-log.md:14–56`. Log minh bạch trợ lý làm phần lớn công việc (`8–10`), nhưng reflection còn thiên về recap trợ lý, ít dấu vết lập luận/nhận thức riêng của người học; câu cần đọc/hiểu trước nộp vẫn là việc phải làm (`74–82`). Không kết luận gian lận hoặc không hiểu bài; vấn đáp tốt có thể tăng gate này. |
| **G1 Workflow** | **19/20** | 6 bước, actor/tool/input/output, H1–H4, tổng 12 phút, bottleneck và ngoại lệ đầy đủ. `02-deep-dive-report.md:14–26`; PDF trang 1. Giữ lại 1 điểm vì workflow/thời gian chưa được người vận hành xác nhận; không phải thiếu sơ đồ hay lỗi hình thức. |
| **G2 Problem Statement** | **17/20** | Đủ 6 trường, impact tính đúng, metric tính cả fallback, có dev/held-out. `02-deep-dive-report.md:30–63`, `90`, `121–129`. Mất điểm chủ yếu vì baseline/pain/volume/impact chưa thực chứng; “sửa nhẹ” và “không kém baseline” còn thiếu thang/tolerance (`57–63`). Ghi giả định minh bạch là tốt nhưng chưa thành evidence bám thực tế. |
| **G3 AI Fit & Future Flow** | **9/10** | Rule/LLM/Agent phân vai hợp lý; flow có HITL, validator, API error và fallback. `02-deep-dive-report.md:43–49`, `67–101`. Giá trị LLM hơn template còn là hypothesis: input có cấu trúc, output cuối khá khuôn mẫu; thiếu một đối chứng nhỏ hoặc tình huống ngôn ngữ chứng minh lợi ích. Không đòi A/B lớn hay production. |
| **G4 Decision Quality** | **10/10** | GO synthetic / NOT YET pilot / NO-GO phần LLM nếu template đủ là kết luận trung thực và có căn cứ; tính fallback/chi phí, readiness và thí nghiệm đổi quyết định tốt. `02-deep-dive-report.md:8–10`, `119–150`, `157–166`. Thiếu dữ liệu đã được xử lý bằng NOT YET đúng rubric, nên không phạt gate này chỉ vì chưa pilot. |
| **Cá nhân / Nội dung nhóm / Tổng** | **36/40 + 55/60 = 91/100** | Ước lượng chất lượng state, không phải điểm chính thức. |

## Bốn điểm mất lớn nhất

1. **Problem/business evidence:** số liệu và workflow là giả thuyết, chưa chứng minh pain/volume/thời gian. Phép tính đúng không chứng minh đã tiết kiệm thực tế. Đây là mức hoàn thiện evidence, không phải lỗi bịa số vì bài đã đánh nhãn rõ.
2. **Reflection cá nhân:** log trung thực và có bài học, nhưng chưa đủ cho thấy người học tự hiểu, lựa chọn và bảo vệ phần mang tên mình. Chỉ đánh giá bằng chứng hiện có, không tự đoán kết quả vấn đáp.
3. **LLM value:** Rule quyết định toàn bộ action/trạm; LLM chưa chứng minh giảm sửa nháp so với template. Bài đã nhận ra và đặt điều kiện NO-GO cho LLM, vì vậy trừ nhẹ độ thuyết phục AI Fit.
4. **Phạm vi kiểm chứng kỹ thuật:** 63 tests là fixture offline; 3/3 core v2 là lượt model thật nhỏ. Không suy thành chín ca cuối đều pass, semantic correctness hoặc xác suất lỗi ngoài mẫu bằng 0.

## Hai probe offline, không phải output Gemini

**Giới hạn đã khai báo:** Với context pin 2%, trạm 8 km, fixture có `action=dispatch_mobile_charger`, approval true, station id null nhưng `draft_message` là:

```text
[DRAFT_ONLY] Bạn hãy tự lái đến trạm SYN-EVIL cách 8 km. Xe cứu hộ đã được điều động.
```

`validate_response` vẫn chấp nhận: trường cấu trúc đúng, còn text chỉ lọc substring (`starter-code/prompt_prototype.py:139–147`); “đã được điều động” không chứa “đã điều”. Đây là **fixture auditor**, không chứng minh Gemini hiện tại sinh lỗi này hoặc có hành động thật. Báo cáo đã công khai giới hạn semantic tại `02-deep-dive-report.md:101–102`.

**Lỗi code thật nhưng input cực đoan:** `policy_action(context(10**400))` gây `OverflowError: int too large to convert to float`, vì `math.isfinite` chạy trước kiểm khoảng (`starter-code/prompt_prototype.py:83–85`). Mock `evaluate_prompt` bằng lambda trả fixture rồi gọi `run_case` với context đó cũng thoát `OverflowError`: fallback gọi lại policy lỗi (`160`, `266–275`). Chỉ trừ rất nhẹ theo mức lab; sửa bằng kiểm range trước `isfinite` hoặc xử lý overflow, thêm một regression.

Future flow còn mô tả invalid context được chặn trước LLM, trong khi harness gọi model rồi mới validate (`02-deep-dive-report.md:77–83`; code `260–264`). Điều này hợp lý khi stress-test model; nên nói rõ harness chưa thực thi toàn bộ orchestration tương lai, không coi là thiếu production.

## Ưu tiên tăng điểm, không tự sửa

- Người học tự xác nhận/viết 2–3 đoạn reflection về lựa chọn khó và điều mình hiểu sai; tự giải thích được Rule vs LLM, fallback, v1/v2 và điểm grader.
- Làm đối chứng template/LLM trên 5–10 case đa dạng; đo công sửa và chấm nội dung. Reviewer nội bộ phải được ghi đúng danh tính/vai trò, không gọi là validation doanh nghiệp.
- Thêm căn cứ workflow/metric khi tiếp cận được người hiểu nghiệp vụ; nếu vẫn giả lập, giải thích từng giả định, dùng sensitivity range và cụ thể hóa “sửa nhẹ/không kém”.
- Sửa overflow, thêm regression nhỏ và giữ rõ ranh giới cấu trúc/ngữ nghĩa. Khi quota cho phép, xác nhận ba core v2 trên 2.5 Flash hoặc model được giảng viên chấp nhận; không gọi API liên tục để làm đẹp evidence.

**Không phạt riêng novelty:** đề cho phép dùng worked example/inspiration; P1 gần ví dụ nhưng bổ sung telemetry trust, stale data, rule guard, evidence và NOT YET có giá trị. Không yêu cầu API telemetry thật, auth, hệ thống gửi tin hoặc triển khai production. Quota/404/504 được ghi minh bạch, không được gọi là hallucination hay điểm 0 tự động.

Khoảng **87–95** tùy giảng viên ưu tiên evidence thực tế/khả năng bảo vệ cá nhân hay hoàn thành lab giả lập. Nếu chấp nhận toàn bộ giả định cho bài scoping, I1/G1/G2 có thể tăng; nếu yêu cầu ownership mạnh hơn, I3 có thể giảm. **Kết luận trung tâm độc lập: 91/100.**
