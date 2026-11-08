# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

### QUICK PROBLEM CARD #1 — VinFast Omnichannel Customer Service

**Bài toán (1 câu):** Nhân viên CSKH mất thời gian tổng hợp ngữ cảnh từ các kênh, tra cứu chính sách và soạn câu trả lời cho các yêu cầu lặp lại.

**Quy trình hiện tại:**

```text
┌────────────────────────────────────────────────────────────┐
│ B1. Tiếp nhận yêu cầu — 0.5 phút                            │
│ Ai: CSKH                                                    │
│ In: Hotline / Email / App / Chat                            │
│ Out: Ticket mới                                             │
└────────────────────────────────────────────────────────────┘
                          │
                          │ 🔄 Handoff: Kênh → Ticket/Agent
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B2. Xác minh & tổng hợp lịch sử — 1.5 phút 🔴               │
│ Ai: CSKH                                                    │
│ In: ID khách hàng, ticket cũ                                │
│ Out: Ngữ cảnh khách hàng                                    │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B3. Tra cứu chính sách / FAQ — 1.0 phút 🔴                  │
│ Ai: CSKH                                                    │
│ In: Vấn đề, KB / tài liệu                                   │
│ Out: Căn cứ trả lời                                         │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B4. Soạn, kiểm tra & gửi phản hồi — 1.5 phút 🔴             │
│ Ai: CSKH                                                    │
│ In: Ngữ cảnh + chính sách                                  │
│ Out: Phản hồi khách hàng                                    │
└────────────────────────────────────────────────────────────┘
                          │
                          │ 🔄 Handoff: Agent → Kênh CSKH
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B5. Cập nhật trạng thái / chuyển tuyến — 0.5 phút          │
│ Ai: CSKH                                                    │
│ In: Kết quả                                                 │
│ Out: Ticket / nhóm phụ trách                                │
└────────────────────────────────────────────────────────────┘
```

**⏱ Tổng cộng = 0.5 + 1.5 + 1.0 + 1.5 + 0.5 = 5.0 phút/ticket.**

**🔴 Điểm nghẽn:**

- B2–B4 chiếm **4/5 phút (80%)** tổng thời gian xử lý.
- Nhân viên mất thời gian tổng hợp lịch sử khách hàng từ nhiều kênh.
- Rủi ro bỏ sót ngữ cảnh, sử dụng chính sách lỗi thời hoặc phản hồi không nhất quán.

**🔄 Handoff:**

- Kênh tiếp nhận → Ticket/Agent.
- Agent → Kênh CSKH.

**Lưu ý:** Các kênh và công cụ nêu trên là giả định tích hợp, cần xác minh mức độ tập trung dữ liệu hiện tại.

---

### QUICK PROBLEM CARD #2 — VinFast Warranty Request Triage

**Bài toán (1 câu):** Nhân viên hậu mãi phải đọc hồ sơ, phân nhóm triệu chứng và đối chiếu điều kiện bảo hành trước khi chuyển chuyên viên xử lý.

**Quy trình hiện tại:**

```text
┌────────────────────────────────────────────────────────────┐
│ B1. Tiếp nhận hồ sơ xe / khách hàng — 2 phút                │
│ Ai: Cố vấn dịch vụ                                          │
│ In: VIN, mô tả lỗi, hình ảnh                                │
│ Out: Hồ sơ bảo hành                                         │
└────────────────────────────────────────────────────────────┘
                          │
                          │ 🔄 Handoff: Tiếp nhận → Hậu mãi
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B2. Đọc mô tả & trích xuất triệu chứng — 4 phút 🔴          │
│ Ai: Nhân viên hậu mãi                                       │
│ In: Văn bản, hình ảnh                                       │
│ Out: Nhóm triệu chứng                                      │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B3. Tra cứu điều khoản & thông tin xe — 4 phút 🔴           │
│ Ai: Nhân viên hậu mãi                                       │
│ In: VIN, KB, lịch sử xe                                     │
│ Out: Gợi ý xử lý                                            │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B4. Gắn nhãn, ghi chú & chuyển chuyên viên — 2 phút         │
│ Ai: Nhân viên hậu mãi                                       │
│ In: Hồ sơ đã rà soát                                        │
│ Out: Ticket triage                                          │
└────────────────────────────────────────────────────────────┘
                          │
                          │ 🔄 Handoff: Hậu mãi → Kỹ thuật
                          ▼
                [Chuyên viên kiểm tra]
```

**⏱ Tổng cộng = 2 + 4 + 4 + 2 = 12 phút/hồ sơ.**

**🔴 Điểm nghẽn:**

- B2 và B3 chiếm **8/12 phút (67%)** tổng thời gian.
- Nhân viên phải đọc mô tả lỗi và tra cứu nhiều tài liệu kỹ thuật.
- Việc thiếu thông tin có thể dẫn đến phân loại sai hoặc phải bổ sung hồ sơ.

**🔄 Handoff:**

- Bộ phận tiếp nhận → Nhân viên hậu mãi.
- Nhân viên hậu mãi → Chuyên viên kỹ thuật.

**Lưu ý:** Phân loại triệu chứng không đồng nghĩa với xác định nguyên nhân hỏng hoặc phê duyệt bảo hành.

---

### QUICK PROBLEM CARD #3 — Vinhomes Resident Request Dispatcher

**Bài toán (1 câu):** Ban quản lý cần đọc phản ánh cư dân, phân loại mức độ ưu tiên và chuyển đúng bộ phận trong thời gian ngắn.

**Quy trình hiện tại:**

```text
┌────────────────────────────────────────────────────────────┐
│ B1. Tiếp nhận phản ánh từ cư dân — 1 phút                   │
│ Ai: Lễ tân / Ban quản lý (BQL)                              │
│ In: App, Hotline, Quầy                                      │
│ Out: Ticket                                                │
└────────────────────────────────────────────────────────────┘
                          │
                          │ 🔄 Handoff: Kênh → BQL
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B2. Đọc mô tả, ảnh & xác định loại sự cố — 2 phút 🔴         │
│ Ai: BQL                                                     │
│ In: Nội dung, căn hộ / tòa nhà                              │
│ Out: Nhóm sự cố                                             │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B3. Đánh giá khẩn cấp & chọn đội phụ trách — 2 phút 🔴      │
│ Ai: BQL                                                     │
│ In: Nhóm sự cố, vị trí, SLA                                 │
│ Out: Mức ưu tiên + đội xử lý                                │
└────────────────────────────────────────────────────────────┘
                          │
                          │ 🔄 Handoff: BQL → Đội thực địa
                          ▼
┌────────────────────────────────────────────────────────────┐
│ B4. Giao việc, xác nhận & cập nhật ticket — 1 phút          │
│ Ai: BQL                                                     │
│ In: Đội nhận việc                                           │
│ Out: Ticket được điều phối                                  │
└────────────────────────────────────────────────────────────┘
```

**⏱ Tổng cộng = 1 + 2 + 2 + 1 = 6 phút/ticket.**

**🔴 Điểm nghẽn:**

- B2–B3 chiếm **4/6 phút (67%)** tổng thời gian điều phối.
- Nội dung phản ánh của cư dân có thể không rõ ràng hoặc thiếu thông tin.
- Rủi ro phân loại sai đội, đánh giá thấp mức độ khẩn cấp hoặc chuyển yêu cầu qua nhiều bộ phận.

**🔄 Handoff:**

- Kênh tiếp nhận → Ban quản lý.
- Ban quản lý → Đội thực địa.

**Lưu ý:** Thời gian trên chỉ tính hoạt động tiếp nhận, phân loại và điều phối, không bao gồm thời gian khắc phục sự cố.

---

### 📊 Tổng hợp Current-State Workflow

| Bài toán                     | Tổng thời gian | Bottleneck | Thời gian bottleneck | Tỷ lệ |
| ---------------------------- | -------------- | ---------- | -------------------- | ----- |
| VinFast Omnichannel CSKH     | 5 phút/ticket  | B2–B4      | 4 phút               | 80%   |
| VinFast Warranty Triage      | 12 phút/hồ sơ  | B2–B3      | 8 phút               | 67%   |
| Vinhomes Resident Dispatcher | 6 phút/ticket  | B2–B3      | 4 phút               | 67%   |

**Kết luận:** Cả ba quy trình đều có điểm nghẽn chủ yếu ở các bước đọc hiểu, tổng hợp thông tin, tra cứu tài liệu hoặc phân loại yêu cầu. Đây là các bước có tiềm năng ứng dụng LLM kết hợp RAG hoặc Rule Engine để hỗ trợ nhân viên, giảm thời gian xử lý và tăng tính nhất quán.
