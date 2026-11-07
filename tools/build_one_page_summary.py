"""Render the one-page artifact pack required by the lecture PDF."""
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# Reuse Vietnamese font registration from the workflow renderer.
from build_workflow_pdf import NAVY, TEAL, INK, MUTED

ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = A4
BODY = WIDTH - 68
STYLES = {
    "title": ParagraphStyle("title", fontName="ArialLab-Bold", fontSize=19, leading=23, textColor=NAVY),
    "subtitle": ParagraphStyle("subtitle", fontName="ArialLab", fontSize=9, leading=12, textColor=MUTED),
    "heading": ParagraphStyle("heading", fontName="ArialLab-Bold", fontSize=10.5, leading=14, textColor=TEAL, spaceBefore=9, spaceAfter=4),
    "body": ParagraphStyle("body", fontName="ArialLab", fontSize=9.1, leading=12.2, textColor=INK),
    "small": ParagraphStyle("small", fontName="ArialLab", fontSize=8.2, leading=10.7, textColor=MUTED),
    "label": ParagraphStyle("label", fontName="ArialLab-Bold", fontSize=9.1, leading=12.2, textColor=NAVY),
    "tablehead": ParagraphStyle("tablehead", fontName="ArialLab-Bold", fontSize=8.6, leading=11.5, textColor=colors.white),
    "cell": ParagraphStyle("cell", fontName="ArialLab", fontSize=8.5, leading=11.3, textColor=INK),
}


def p(text, style="body"):
    return Paragraph(text, STYLES[style])


def footer(c, doc):
    if doc.page != 1:
        raise ValueError("Artifact pack overflowed beyond one page")
    c.setStrokeColor(colors.HexColor("#D2DDE7"))
    c.line(34, 31, WIDTH - 34, 31)
    c.setFillColor(MUTED)
    c.setFont("ArialLab", 7.5)
    c.drawString(34, 20, "Hoàng Bảo Nguyên | 2A202603384 | Day 02 | 07/11/2026")
    c.drawRightString(WIDTH - 34, 20, "Artifact pack / 1 trang")


def main():
    live = json.loads((ROOT / "evidence/live-results.json").read_text(encoding="utf-8"))
    output = ROOT / "05-one-page-artifact-pack.pdf"
    doc = SimpleDocTemplate(str(output), pagesize=A4, topMargin=29, bottomMargin=40,
                            leftMargin=34, rightMargin=34,
                            title="Day02 - One-page artifact pack - Hoàng Bảo Nguyên",
                            author="Hoàng Bảo Nguyên / 2A202603384")
    story = [p("Xanh SM / Incident Drafting", "title"),
             p("Hoàng Bảo Nguyên - 2A202603384 | Rule + workflow cố định, thử LLM feature", "subtitle"),
             Spacer(1, 7),
             p("<b>GO</b> prototype mô phỏng; <b>NOT YET</b> pilot thật. Baseline và business impact là giả định discovery; chưa có dữ liệu doanh nghiệp hoặc đánh giá operator.", "body"),
             p("01 / Problem Statement", "heading")]
    data = [
        [p("Actor", "label"), p("Điều phối viên xử lý sự cố pin; trưởng ca duyệt ngoại lệ; tài xế nhận phản hồi.")],
        [p("Workflow", "label"), p("Nhận tin → xác minh pin/độ mới → tra trạm/quy trình → soạn → duyệt/gửi → ghi log. Baseline giả định: 12 phút/case.")],
        [p("Bottleneck", "label"), p("Tra cứu + soạn: 6/12 phút; lời nhắn có thể thiếu hoặc mâu thuẫn telemetry.")],
        [p("Impact", "label"), p("Giả định 12 case/ngày ×26 ngày =312 case/tháng; 62,4 giờ xử lý theo case. Chưa là thời gian hoặc thiệt hại đã đo.")],
        [p("Success", "label"), p("Mục tiêu ≤5 phút/case đủ dữ liệu; ≥80% nháp chấp nhận sửa nhẹ; 100% hành động cần người duyệt. Tính cả fallback; rubric Q1-Q4 và thời gian sửa phải đo với người dùng.")],
        [p("Boundary", "label"), p("Rule quyết định nhánh, LLM chỉ nháp. Không gửi/điều xe thật, không bịa trạm hay bảo đảm khả năng lái an toàn. Thiếu/cũ/lỗi → người xử lý; ngưỡng 5%/5 km là policy lab.")],
    ]
    table = Table(data, colWidths=[72, BODY - 72], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E9F1F6")),
        ("BACKGROUND", (1, 0), (-1, -1), colors.HexColor("#F7F9FB")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#D4DEE7")),
    ]))
    story += [table, p("02 / RACI-lite đề xuất", "heading")]
    rows = [[p(x, "tablehead") for x in ["Hoạt động", "R - thực hiện", "A - chịu trách nhiệm", "C - tham vấn"]]]
    for row in [
        ["Problem / metric", "Operator", "Ops owner", "AI / Data"],
        ["Build / eval", "AI / Data", "Ops owner", "Operator / Risk"],
        ["Duyệt / hành động", "Operator", "Trưởng ca", "Risk khi ngoại lệ"],
        ["Dừng AI / rollback", "Operator / Platform", "Ops owner", "AI / Risk"],
    ]:
        rows.append([p(x, "cell") for x in row])
    raci = Table(rows, colWidths=[125, 130, 142, BODY - 397], hAlign="LEFT")
    raci.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F1F5F8"), colors.white]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [raci, p("03 / AI Readiness và gate", "heading"),
              p("<b>Có:</b> fixture, rule/prompt/validator, fallback và evidence kỹ thuật. <b>Chưa:</b> baseline/log thật, nhãn SME, operator review, A/B thời gian sửa và owner xác nhận. <b>NO-GO phần LLM</b> nếu template đạt chất lượng tương đương với công sức/chi phí thấp hơn."),
              p("04 / Next experiment nhỏ nhất", "heading"),
              p("Kế hoạch hai ngày: (1) xác nhận workflow và đo 30 case ẩn danh; (2) chốt policy/RACI và nhãn; (3) so template/LLM ghép cặp bằng Q1-Q4 và thời gian sửa thật; (4) chỉ mở shadow pilot khi gate đạt, owner xác nhận và rollback đã thử. Chưa tự gửi hành động."),
              Spacer(1, 8),
              p(f"<b>Evidence:</b> 82 test offline; live core {live['passed']}/{live['cases']} trên {live['model']}; prompt v2 / validator v3. Đối chứng ba output đã lưu: template và LLM đều qua contract, chưa chứng minh lợi ích LLM hơn template. Chi tiết: báo cáo và evidence/submission-verification.md.", "small")]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(str(output))


if __name__ == "__main__":
    main()
