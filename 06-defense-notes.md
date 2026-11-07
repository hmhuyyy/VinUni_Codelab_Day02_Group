# Ghi chú chuẩn bị giải thích bài - Hoàng Bảo Nguyên

Đây là tài liệu ôn bài, không phải biên bản vấn đáp hoặc chứng nhận người học đã nắm hết nội dung.

| Câu hỏi | Ý chính cần giải thích bằng lời của mình |
|---|---|
| Bài toán cụ thể là gì? | Điều phối viên mất công xác minh và soạn phản hồi sự cố pin; giới hạn ở nháp và kiểm tra context, không tự vận hành đội xe |
| 12 phút và 12 case/ngày từ đâu? | Là giả định thiết kế có nhãn, chưa có log doanh nghiệp. Dùng công thức để kiểm tra logic và lập kế hoạch đo; không nhận là thống kê thật |
| Vì sao dùng Rule + LLM, chưa cần Agent? | Action/trạm có điều kiện cứng và luồng cố định. Rule/template là baseline; LLM chỉ thử diễn đạt. Không có nhu cầu tự chọn tool hoặc vòng lặp tự trị |
| Template đã đủ thì sao? | Đối chứng ba case đạt cùng contract chưa cho thấy ưu thế LLM. Nếu chất lượng/công sửa không tốt hơn, bỏ LLM và giữ template |
| Pin dưới 5% có nghĩa gì? | Policy lab chọn đề xuất cứu hộ; không phải mô hình ước lượng quãng đường hay chứng minh xe có thể lái an toàn |
| Khi dữ liệu thiếu hoặc model lỗi? | Escalate/fallback sang người. Raw response lỗi vẫn fail; fallback không biến thành model pass; không có tool gửi/điều xe thật |
| Khác nhau giữa prompt v2 và validator v3? | Prompt v2 sửa câu hứa quá mức. Validator v3 sửa overflow và bổ sung regression từ audit; ghi hai phiên bản riêng để tránh gộp evidence sai |
| Vì sao đổi model? | Default vẫn 2.5 Flash theo worksheet. Key chạm quota ngày của model đó; 2.5 Lite trả 404, API chỉ định 3.5 Lite. Evidence ghi đúng tên; đề không nêu chế tài đổi model |
| 82 test và 3/3 live chứng minh gì? | Offline xác nhận code/fixture/SDK wiring; live là output model thật của ba ca lõi. Chưa chứng minh accuracy toàn bộ case, semantic quality với operator hoặc ROI |
| Vì sao NOT YET dù autograder qua? | Thiếu baseline thật, nhãn domain và chấp thuận vận hành. Autograder kiểm kỹ thuật; pilot cần gate business/ops/data |
| Bạn đóng góp gì cho nhóm? | Candidate có workflow/metric/boundary, code cá nhân, evidence và phản biện. Nhóm vẫn phải chọn bài chung; trưởng nhóm tổng hợp báo cáo lên main và điền form |

Trước khi trình bày, tự mở code và chỉ được vị trí: `policy_action`, `validate_response`, `safe_fallback`, `evaluate_prompt`; giải thích một case pin 2% và một case pin 5%. Nếu còn chưa hiểu phần nào, hỏi lại và sửa reflection theo hiểu biết thật thay vì nhận đã làm hoạt động chưa diễn ra.
