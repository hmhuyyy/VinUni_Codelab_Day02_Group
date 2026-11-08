# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

## 📝 1. Danh sách bài toán của tôi

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | VinFast – Omnichannel Customer Service | Repetitive + AI-upgrade | Nhân viên phải tổng hợp lịch sử khách hàng từ nhiều kênh và xử lý câu hỏi lặp lại |
| 2 | VinFast – Phân loại yêu cầu bảo hành | Time-consuming | Đọc mô tả lỗi, đối chiếu chính sách, xác định nhóm xử lý |
| 3 | Xanh SM – Xử lý khiếu nại chuyến đi | Stakeholder Pain | Kiểm tra GPS, lịch sử chuyến đi, giao dịch và phản hồi của tài xế |
| 4 | Vinhomes – Phân loại yêu cầu cư dân | Repetitive | Tiếp nhận, phân loại và chuyển yêu cầu sửa chữa, vệ sinh, an ninh |
| 5 | Vinmec – Tóm tắt hồ sơ trước khám | Time-consuming + AI-upgrade | Bác sĩ hoặc nhân viên phải đọc, tổng hợp thông tin từ nhiều tài liệu |

## 📊 2. Ước tính khối lượng và chi phí vận hành

**Giả định:**
- Chi phí nhân sự xử lý nghiệp vụ: **60.000 VNĐ/giờ**.
- Số ngày vận hành: **26 ngày/tháng**.
- Số lượng yêu cầu và thời gian xử lý là giả định để xây dựng business case.

| # | Bài toán | Khối lượng giả định | Thời gian thủ công | Giờ công/tháng | Chi phí quy đổi/tháng |
|---|---|---|---|---|---|
| 1 | Omnichannel CSKH | 3.000 ticket/ngày | 5 phút/ticket | 6.500 giờ | 390 triệu VNĐ |
| 2 | Phân loại bảo hành | 500 hồ sơ/ngày | 12 phút/hồ sơ | 2.600 giờ | 156 triệu VNĐ |
| 3 | Khiếu nại chuyến đi | 1.000 case/ngày | 8 phút/case | 3.467 giờ | 208 triệu VNĐ |
| 4 | Yêu cầu cư dân | 1.500 ticket/ngày | 6 phút/ticket | 3.900 giờ | 234 triệu VNĐ |
| 5 | Tóm tắt hồ sơ khám | 300 hồ sơ/ngày | 10 phút/hồ sơ | 1.300 giờ | 78 triệu VNĐ |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

## 🃏 QUICK PROBLEM CARD #1

### 1. Thông tin bài toán

**Bài toán (1 câu):** Omnichannel Customer Service – Hỗ trợ nhân viên CSKH VinFast tổng hợp thông tin khách hàng đa kênh và xử lý các yêu cầu lặp lại.

**Công ty thành viên:**
- [x] VinFast
- [ ] Xanh SM
- [ ] Vinhomes
- [ ] Vinmec
- [ ] Khác

**Ai đang đau (Actor)?**
- Nhân viên chăm sóc khách hàng (CSKH).
- Trưởng nhóm CSKH.
- Khách hàng VinFast.

### 2. Workflow thủ công hiện tại

1. **Tiếp nhận yêu cầu:** Nhận thông tin từ Hotline, Email, App hoặc Web Chat.
2. **Tra cứu thông tin:** Tìm kiếm lịch sử khách hàng, ticket và chính sách liên quan.
3. **Soạn phản hồi:** Giải thích vấn đề và hướng dẫn khách hàng xử lý.
4. **Gửi phản hồi:** Gửi nội dung cho khách hàng và cập nhật trạng thái ticket.

**Bước tốn thời gian/lỗi nhất:**
- Bước 2 và bước 3.
- Thời gian xử lý thủ công giả định: **5 phút/ticket**.
- Nhân viên phải tra cứu nhiều hệ thống và tổng hợp thông tin trước khi phản hồi.

### 3. AI có thể hỗ trợ ở bước nào?

**Bước 2–3: Tra cứu thông tin và soạn phản hồi.**

- **LLM:** Hiểu nội dung yêu cầu, tóm tắt lịch sử hội thoại và đề xuất câu trả lời.
- **RAG:** Truy xuất chính sách, tài liệu hướng dẫn và thông tin liên quan.
- **Human-in-the-loop:** Nhân viên kiểm duyệt nội dung trước khi gửi khách hàng.

### 4. Đo thành công bằng gì (Metrics)?

| Metric | Hiện tại | Mục tiêu |
|---|---|---|
| Thời gian xử lý trung bình | 5 phút/ticket | ≤ 2 phút/ticket |
| Tỷ lệ giảm thời gian xử lý | 0% | ≥ 60% |
| Intent Classification Accuracy | Chưa đo | ≥ 90% trên tập test |

### 5. Quick Architecture

**Phương án công nghệ:**
- [ ] No AI
- [ ] Rule
- [x] LLM
- [ ] Agent

**Kiến trúc đề xuất:**

`Omnichannel Gateway → Customer Context → RAG/LLM → Agent Copilot → Human Approval`

**Giải thích:** Hệ thống tập hợp dữ liệu từ nhiều kênh, truy xuất ngữ cảnh khách hàng và tài liệu liên quan, sau đó sử dụng LLM đề xuất phản hồi để nhân viên phê duyệt.

---

## 🃏 QUICK PROBLEM CARD #2

### 1. Thông tin bài toán

**Bài toán (1 câu):** Nhân viên hậu mãi VinFast phải đọc mô tả lỗi, đối chiếu chính sách bảo hành và phân loại hồ sơ thủ công.

**Công ty thành viên:**
- [x] VinFast
- [ ] Xanh SM
- [ ] Vinhomes
- [ ] Vinmec
- [ ] Khác

**Ai đang đau (Actor)?**
- Nhân viên bảo hành.
- Cố vấn dịch vụ.
- Kỹ thuật viên.
- Chủ xe VinFast.

### 2. Workflow thủ công hiện tại

1. **Nhận hồ sơ lỗi:** Tiếp nhận mô tả lỗi, hình ảnh và thông tin xe.
2. **Phân loại lỗi:** Đọc nội dung và xác định nhóm lỗi hoặc triệu chứng.
3. **Tra cứu chính sách:** Đối chiếu điều kiện và chính sách bảo hành.
4. **Chuyển hồ sơ:** Chuyển hồ sơ cho kỹ thuật viên hoặc bộ phận xử lý phù hợp.

**Bước tốn thời gian/lỗi nhất:**
- Bước 2 và bước 3.
- Thời gian xử lý thủ công giả định: **12 phút/hồ sơ**.
- Nhân viên phải đọc thông tin kỹ thuật và đối chiếu nhiều điều kiện bảo hành.

### 3. AI có thể hỗ trợ ở bước nào?

**Bước 2–3: Phân loại lỗi và tra cứu chính sách bảo hành.**

- **LLM:** Phân tích mô tả triệu chứng và đề xuất nhóm lỗi.
- **RAG:** Truy xuất chính sách bảo hành, tài liệu kỹ thuật liên quan.
- **Rule Engine:** Kiểm tra các điều kiện bảo hành dựa trên quy tắc nghiệp vụ.
- **Human-in-the-loop:** Nhân viên kiểm tra và phê duyệt kết quả trước khi chuyển hồ sơ.

### 4. Đo thành công bằng gì (Metrics)?

| Metric | Hiện tại | Mục tiêu |
|---|---|---|
| Thời gian phân loại hồ sơ | 12 phút/hồ sơ | ≤ 5 phút/hồ sơ |
| Tỷ lệ giảm thời gian xử lý | 0% | ≥ 58% |
| Classification F1-score | Chưa đo | ≥ 90% so với nhãn chuyên gia |

### 5. Quick Architecture

**Phương án công nghệ:**
- [ ] No AI
- [x] Rule
- [x] LLM
- [ ] Agent

**Kiến trúc đề xuất:**

`Warranty Request → LLM Classification → RAG Policy Retrieval → Rule Engine → Human Approval → Technician`

**Giải thích:** LLM phân tích mô tả lỗi, RAG truy xuất chính sách liên quan, Rule Engine kiểm tra điều kiện bảo hành và nhân viên phê duyệt kết quả trước khi chuyển bộ phận kỹ thuật.

---

## 🃏 QUICK PROBLEM CARD #3

### 1. Thông tin bài toán

**Bài toán (1 câu):** Ban quản lý Vinhomes mất nhiều thời gian phân loại và điều phối phản ánh của cư dân tới đúng bộ phận xử lý.

**Công ty thành viên:**
- [ ] VinFast
- [ ] Xanh SM
- [x] Vinhomes
- [ ] Vinmec
- [ ] Khác

**Ai đang đau (Actor)?**
- Nhân viên ban quản lý.
- Đội kỹ thuật.
- Đội vệ sinh.
- Bộ phận an ninh.
- Cư dân Vinhomes.

### 2. Workflow thủ công hiện tại

1. **Tiếp nhận phản ánh:** Nhận yêu cầu từ ứng dụng, hotline hoặc lễ tân.
2. **Phân loại yêu cầu:** Đọc nội dung và xác định loại sự cố.
3. **Xác định ưu tiên:** Đánh giá mức độ khẩn cấp và chọn đội xử lý.
4. **Giao việc:** Chuyển yêu cầu tới bộ phận phụ trách và cập nhật trạng thái.

**Bước tốn thời gian/lỗi nhất:**
- Bước 2 và bước 3.
- Thời gian xử lý thủ công giả định: **6 phút/ticket**.
- Dễ xảy ra tình trạng phân loại sai hoặc chuyển yêu cầu không đúng bộ phận.

### 3. AI có thể hỗ trợ ở bước nào?

**Bước 2–3: Phân loại yêu cầu và điều phối xử lý.**

- **LLM:** Trích xuất loại sự cố, vị trí và nội dung chính từ phản ánh.
- **Rule Engine:** Xác định mức độ ưu tiên và đề xuất đội xử lý phù hợp.
- **Human-in-the-loop:** Nhân viên kiểm tra các trường hợp không rõ ràng hoặc có mức độ khẩn cấp cao.

### 4. Đo thành công bằng gì (Metrics)?

| Metric | Hiện tại | Mục tiêu |
|---|---|---|
| Thời gian phân loại và điều phối | 6 phút/ticket | ≤ 2 phút/ticket |
| Tỷ lệ giảm thời gian xử lý | 0% | ≥ 67% |
| Routing Accuracy | Chưa đo | ≥ 95% |

### 5. Quick Architecture

**Phương án công nghệ:**
- [ ] No AI
- [x] Rule
- [x] LLM
- [ ] Agent

**Kiến trúc đề xuất:**

`Resident Request → LLM Extraction → Rule-based Priority & Routing → Human Review → Assigned Team`

**Giải thích:** LLM trích xuất thông tin từ phản ánh của cư dân, Rule Engine xác định mức độ ưu tiên và bộ phận phụ trách, sau đó chuyển yêu cầu đến đội xử lý phù hợp.

---

## 📌 Tổng kết Phase 2

| Tiêu chí | Card #1 – VinFast CSKH | Card #2 – VinFast Bảo hành | Card #3 – Vinhomes |
|---|---|---|---|
| Khối lượng/ngày | 3.000 ticket | 500 hồ sơ | 1.500 ticket |
| Thời gian hiện tại | 5 phút | 12 phút | 6 phút |
| Thời gian mục tiêu | ≤ 2 phút | ≤ 5 phút | ≤ 2 phút |
| Mức giảm mục tiêu | 60% | 58% | 67% |
| Công nghệ | LLM + RAG | LLM + RAG + Rule | LLM + Rule |
| Metric chất lượng | Intent Accuracy ≥ 90% | F1 ≥ 90% | Routing Accuracy ≥ 95% |

**Ghi chú:** Các số liệu về khối lượng, thời gian, chi phí và KPI mục tiêu trong tài liệu là giả định phục vụ đánh giá sơ bộ, chưa phải kết quả đo lường thực tế.