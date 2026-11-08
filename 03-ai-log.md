# 📝 Danh sách Prompt sử dụng AI

## Prompt 1 — Phase 1: SCAN

### 1.1. Yêu cầu tìm bài toán theo 4 Lenses

"Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup

1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).

2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).

3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).

4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec].

Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất.

Trong đó có 1 bài toán liên quan đến customer service (omnichannel)."

---

## Prompt 2 — Phase 2: QUICK-ASSESS

"Chọn **top 3 bài toán** sau:

1. Vinhomes Resident Request Dispatcher.
2. VinFast Warranty Request Triage.
3. VinFast Omnichannel Customer Service.

Hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

### QUICK PROBLEM CARD — Template

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #___                                     │
│                                                             │
│ Bài toán (1 câu): _________________________________________ │
│                                                             │
│ Công ty thành viên:                                         │
│ [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes                      │
│ [ ] Vinmec   [ ] Khác (Ghi rõ): __________                  │
│                                                             │
│ Ai đang đau (Actor)? _____________________________________ │
│                                                             │
│ Workflow thủ công hiện tại (3–5 bước):                     │
│ 1. ___ → 2. ___ → 3. ___ → 4. ___                           │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ ___ (⏱ ___ phút/lượt)                                       │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ ___________________________________________________________ │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ ___________________________________________________________ │
│                                                             │
│ VD: Giảm thời gian soạn phản hồi từ 10 min → dưới 2 min     │
│                                                             │
│ Quick Architecture:                                         │
│ [ ] No AI  [ ] Rule  [ ] LLM  [ ] Agent                     │
└─────────────────────────────────────────────────────────────┘
```

Tạo file Markdown."

---

## Prompt 3 — Phase 3: DEEP-DIVE

"Đây là yêu cầu:

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

**Vẽ quy trình hiện tại.** Sử dụng các ký hiệu:

- 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
- 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
- Ghi rõ thời gian vận hành trung bình: **Tổng cộng = \_\_\_\_ phút/lượt**.

## 3.2. Problem Statement (6-field) & Metrics

Điền đầy đủ 6 trường thông tin của bài toán:

| Field                       | Nội dung chi tiết                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------ |
| **1. Actor / Operator**     | Ai đang thực hiện tác vụ hằng ngày?                                                  |
| **2. Current Workflow**     | Mô tả tóm tắt quy trình thủ công hiện tại và công cụ sử dụng.                        |
| **3. Bottleneck**           | Bước nào chậm, lỗi, hoặc cần xử lý ngôn ngữ tự động nhiều nhất?                      |
| **4. Business Impact**      | Tổn thất thực tế đo bằng thời gian, chi phí, hoặc SLA của Vingroup.                  |
| **5. Success Metric**       | AI giải quyết được thì đạt ngưỡng số mấy? (Ví dụ: _85% vé được phân loại dưới 10s_). |
| **6. Operational Boundary** | AI được phép làm gì, TUYỆT ĐỐI không được làm gì, điểm nào cần duyệt?                |

## 3.3. Future-State Flow & AI Fit

- **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào?
  - [ ] Rule / State-Machine
  - [ ] LLM Feature
  - [ ] Agentic Loop

- **Vẽ Future-State Flow:** Đánh dấu rõ:
  - 🔵 **AI Step:** Tác vụ LLM xử lý.
  - 🟢 **Human Step (HITL):** Bước con người phê duyệt/review (Human-in-the-loop).
  - ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.

---

# 📋 Ví dụ tham khảo — Xanh SM Dispatcher

## 3.1. Current-State Workflow

Quy trình xử lý sự cố hết pin thực địa hiện tại của điều phối viên Xanh SM:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn văn bản │
│ gọi sự cố    │ ──→ │ vị GPS xe    │ ──→ │ sạc VinFast  │ ──→ │ hướng dẫn    │
│              │     │              │     │ còn trụ trống│     │ gửi tài xế   │
│ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │
│ ⏱ 2 phút     │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │
│ In: Điện thoại│    │ In: Biển số  │     │ In: Vị trí GPS│    │ In: Raw data │
│ Out: Log sự cố│    │ Out: Tọa độ  │     │ Out: Địa chỉ │     │ Out: SMS     │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                    │
                                                                    ▼
                                                             ┌──────────────┐
                                                             │ Bước 5       │
                                                             │ Gọi xe cứu   │
                                                             │ hộ (nếu cần) │
                                                             │ Ai: Dispatch │
                                                             │ ⏱ 1 phút     │
                                                             └──────────────┘

🔴 = Bottlenecks

⏱ Tổng thời gian xử lý thủ công: 15 phút/lượt.
```

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field                       | Nội dung                                                                                                                                                                                                                                                                                       |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Actor / Operator**     | Điều phối viên (Dispatcher) thuộc Trung tâm Điều vận Xanh SM.                                                                                                                                                                                                                                  |
| **2. Current Workflow**     | Khi tài xế báo hết pin, điều phối viên tra cứu vị trí định vị trên bản đồ nội bộ, mở Dashboard trạm sạc VinFast để tìm trụ sạc trống gần nhất, viết tin nhắn chỉ dẫn/định vị gửi qua App tài xế, và gọi cứu hộ nếu pin dưới 5%. 5 bước, hoàn toàn thủ công, mất 15 phút/lượt.                  |
| **3. Bottleneck**           | Bước 3 & 4 (mất 10 phút): Tra cứu thủ công trụ sạc trống phù hợp với dòng xe (VF5/VFe34/VF8) và soạn thảo tin nhắn hướng dẫn đường đi chi tiết bằng tiếng Việt thân thiện.                                                                                                                     |
| **4. Business Impact**      | Mỗi ngày có ~80 sự cố pin thực địa tại Hà Nội. Gây lãng phí 20 giờ làm việc/ngày của team điều vận. Tăng thời gian chờ đợi của tài xế, dẫn đến rò rỉ doanh thu ~15% do xe không thể đón khách và tài xế bị stress.                                                                             |
| **5. Success Metric**       | 1. Giảm tổng thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút (Efficiency). 2. Tỉ lệ hướng dẫn đúng địa điểm và đúng loại trụ sạc phù hợp đạt 98% (Quality).                                                                                                                                 |
| **6. Operational Boundary** | AI được phép truy xuất API định vị xe, API trạm sạc VinFast trống, tự động soạn thảo tin nhắn hướng dẫn dạng nháp (draft). **CẤM:** AI không được tự động gửi tin đi mà không có điều phối viên phê duyệt (bắt buộc HITL); không được đề xuất trạm sạc không phù hợp với loại cổng sạc của xe. |

---

## 3.3. Future-State Flow & AI Fit

**AI Fit:** Chọn **LLM Feature** (không cần Agent tự trị vì quy trình có cấu trúc cố định, rủi ro khi điều phối sai trạm sạc có thể khiến xe cạn kiệt pin giữa đường và gây tắc nghẽn giao thông).

**Quy trình tương lai (Future-State):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ 🔵 Auto-pull │     │ 🔵 AI draft  │     │ 🟢 Dispatch  │
│ gọi sự cố    │ ──→ │ vị trí &     │ ──→ │ SMS chỉ dẫn  │ ──→ │ click duyệt  │
│              │     │ trạm sạc trống│    │ & chỉ đường │     │ & gửi tài xế │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                    │
                                                                    ▼
                                                               ↩️ Fallback:
                                                               Nếu AI draft lỗi,
                                                               Dispatcher tự viết
                                                               tay lại như cũ.
```

"

---

# 📝 Reflection — Ghi nhận cá nhân

- AI đã giúp tôi tiết kiệm thời gian soạn thảo và chuẩn hóa tài liệu.
- AI là một công cụ hỗ trợ đắc lực, giúp khám phá, gợi ý các ý tưởng và thiết kế các giải pháp.
- AI giúp ta đi nhanh từ ý tưởng tới tài liệu có cấu trúc.
- Tuy nhiên, cần phải **validate lại thông tin mà AI đưa ra**.
