# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

### 📝 List bài toán của tôi:

| #   | Subsidiary (VinFast/Xanh SM...)        | Lens                        | Mô tả ngắn bài toán                                                               |
| --- | -------------------------------------- | --------------------------- | --------------------------------------------------------------------------------- |
| 1   | VinFast – Omnichannel Customer Service | Repetitive + AI-upgrade     | Nhân viên phải tổng hợp lịch sử khách hàng từ nhiều kênh và xử lý câu hỏi lặp lại |
| 2   | VinFast – Phân loại yêu cầu bảo hành   | Time-consuming              | Đọc mô tả lỗi, đối chiếu chính sách, xác định nhóm xử lý                          |
| 3   | Xanh SM – Xử lý khiếu nại chuyến đi    | Stakeholder Pain            | Kiểm tra GPS, lịch sử chuyến đi, giao dịch và phản hồi của tài xế                 |
| 4   | Vinhomes – Phân loại yêu cầu cư dân    | Repetitive                  | Tiếp nhận, phân loại và chuyển yêu cầu sửa chữa, vệ sinh, an ninh                 |
| 5   | Vinmec – Tóm tắt hồ sơ trước khám      | Time-consuming + AI-upgrade | Bác sĩ hoặc nhân viên phải đọc, tổng hợp thông tin từ nhiều tài liệu              |

Giả định chi phí nhân sự xử lý nghiệp vụ là 60.000 VNĐ/giờ, 26 ngày vận hành/tháng. Số lượng yêu cầu và thời gian xử lý là giả định để xây dựng business case.

| # | Bài toán | Khối lượng giả định | Thời gian thủ công | Giờ công/tháng | Chi phí quy đổi/tháng |
|-----------------------------------------------------------------------------
| 1 |Omnichannel CSKH |3.000 ticket/ngày |5 phút/ticket |6.500 giờ|390 triệu|
| 2 |Phân loại bảo hành|500 hồ sơ/ngày |12 phút/hồ sơ |2.600 giờ |156 triệu|
| 3 |Khiếu nại chuyến đi |1.000 case/ngày|8 phút/case |3.467 giờ|208 triệu|
| 4 |Yêu cầu cư dân |1.500 ticket/ngày |6 phút/ticket |3.900 giờ |234 triệu|
| 5 |Tóm tắt hồ sơ khám |300 hồ sơ/ngày |10 phút/hồ sơ |1.300 giờ|78 triệu|

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 │
│ │
│ Bài toán (1 câu): Omnichannel Customer Service │
│ Công ty thành viên: [x] VinFast [ ] Xanh SM [ ] Vinhomes │
│ [ ] Vinmec [ ] Khác (Ghi rõ)**\_\_\_\_** │
│ │
│ Ai đang đau (Actor)? Nhân viên CSKH, trưởng nhóm CSKH và │
│ khách hàng VinFast │
│ │
│ Workflow thủ công hiện tại (3-5 bước): │
│ 1. Tiếp nhận yêu cầu Hotline / Email / App / Web Chat |
| ──> 2. Tra cứu thông tin |
| Lịch sử khách hàng, ticket, chính sách |
| ──> 3. Soạn phản hồi |
| Giải thích, hướng dẫn xử lý |
| ──> 4. Gửi phản hồi và cập nhật ticket │
│ │
│ Bước nào tốn thời gian/lỗi nhất? 2+3 (⏱ 5 phút/lượt) |
│ AI có thể nhảy vào hỗ trợ ở bước nào?LLM + RAG truy xuất |
| tài liệu, tóm tắt lịch sử hội thoại và đề xuất phản hồi theo|
| ngữ cảnh. Nhân viên kiểm duyệt trước khi gửi │
│ │
│ Đo thành công bằng gì (Metric có số)? **********\_\_**********│
│ Thời gian xử lý5 → 2 phút Giảm 60% │
| Intent Accuracy≥90% Trên bộ dữ liệu test |
│ │
│ Quick Architecture: [ ] No AI [ ] Rule [x] LLM [ ] Agent │
| Thành phần: Omnichannel Gateway → Customer Context |
| → RAG/LLM → Agent Copilot → Human Approval. |
└─────────────────────────────────────────────────────────────┘

---

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2 │
│ │
│ Bài toán (1 câu): Nhân viên hậu mãi VinFast phải đọc mô tả │
│ lỗi, đối chiếu bảo hành và phân loại hồ sơ thủ công. │
│ │
│ Công ty thành viên: [x] VinFast [ ] Xanh SM [ ] Vinhomes │
│ [ ] Vinmec [ ] Khác │
│ │
│ Ai đang đau (Actor)? Nhân viên bảo hành, cố vấn dịch vụ, │
│ kỹ thuật viên và chủ xe. │
│ │
│ Workflow thủ công hiện tại (4 bước): │
│ 1. Nhận hồ sơ lỗi (mô tả, ảnh, thông tin xe) │
│ ──> 2. Đọc và xác định nhóm lỗi │
│ ──> 3. Tra cứu chính sách bảo hành │
│ ──> 4. Chuyển hồ sơ cho kỹ thuật viên │
│ │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–3 (⏱ 12 phút/hồ sơ)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2–3: LLM phân │
│ loại triệu chứng, RAG tra cứu, Rule kiểm tra điều kiện. │
│ Nhân viên vẫn phê duyệt kết quả. │
│ │
│ Đo thành công bằng gì (Metric có số)? │
│ Giảm thời gian 12 phút ──> ≤ 5 phút/hồ sơ (−58%); │
│ Classification F1 ≥ 90% so với nhãn chuyên gia. │
│ │
│ Quick Architecture: [ ] No AI [x] Rule [x] LLM [ ] Agent │
└─────────────────────────────────────────────────────────────┘

---

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3 │
│ │
│ Bài toán (1 câu): Ban quản lý Vinhomes mất thời gian phân │
│ loại và điều phối phản ánh cư dân tới đúng bộ phận. │
│ │
│ Công ty thành viên: [ ] VinFast [ ] Xanh SM [x] Vinhomes │
│ [ ] Vinmec [ ] Khác │
│ │
│ Ai đang đau (Actor)? Nhân viên ban quản lý, đội kỹ thuật, │
│ vệ sinh, an ninh và cư dân. │
│ │
│ Workflow thủ công hiện tại (4 bước): │
│ 1. Nhận phản ánh (app/hotline/lễ tân) │
│ ──> 2. Đọc nội dung và phân loại │
│ ──> 3. Xác định độ ưu tiên và đội xử lý │
│ ──> 4. Giao việc và cập nhật trạng thái │
│ │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2–3 (⏱ 6 phút/ticket) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2–3: LLM trích │
│ xuất loại sự cố/vị trí, Rule gợi ý ưu tiên và đội xử lý. │
│ │
│ Đo thành công bằng gì (Metric có số)? │
│ Giảm thời gian 6 phút ──> ≤ 2 phút/ticket (−67%); │
│ Routing Accuracy ≥ 95%. │
│ │
│ Quick Architecture: [ ] No AI [x] Rule [x] LLM [ ] Agent │
└─────────────────────────────────────────────────────────────┘
