"""Recreate the two-page Vietnamese workflow diagram using ReportLab."""
import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path(os.environ.get("LAB_FONT_DIR", "C:/Windows/Fonts"))
pdfmetrics.registerFont(TTFont("ArialLab", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("ArialLab-Bold", str(FONT_DIR / "arialbd.ttf")))
pdfmetrics.registerFontFamily("ArialLab", normal="ArialLab", bold="ArialLab-Bold")

W, H = landscape(A3)
NAVY = colors.HexColor("#142C44")
INK = colors.HexColor("#20364A")
MUTED = colors.HexColor("#586B7C")
BG = colors.HexColor("#F5F8FB")
BLUE = colors.HexColor("#2467A5")
TEAL = colors.HexColor("#087F72")
ORANGE = colors.HexColor("#B64C16")
PURPLE = colors.HexColor("#6541A5")


def paragraph(c, text, x, top, width, size=12, color=INK, bold=False,
              max_height=1000, align=TA_LEFT):
    style = ParagraphStyle("local", fontName="ArialLab-Bold" if bold else "ArialLab",
                           fontSize=size, leading=size * 1.42, textColor=color,
                           alignment=align)
    p = Paragraph(text, style)
    _, height = p.wrap(width, max_height)
    if height > max_height:
        raise ValueError(f"Text overflow ({height} > {max_height}): {text[:60]}")
    p.drawOn(c, x, top - height)
    return height


def arrow(c, x1, y1, x2, y2, color=BLUE):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(1.7)
    c.line(x1, y1, x2, y2)
    path = c.beginPath()
    if abs(x2 - x1) >= abs(y2 - y1):
        direction = 1 if x2 > x1 else -1
        path.moveTo(x2, y2)
        path.lineTo(x2 - direction * 7, y2 + 4)
        path.lineTo(x2 - direction * 7, y2 - 4)
    else:
        direction = 1 if y2 > y1 else -1
        path.moveTo(x2, y2)
        path.lineTo(x2 - 4, y2 - direction * 7)
        path.lineTo(x2 + 4, y2 - direction * 7)
    path.close()
    c.drawPath(path, fill=1, stroke=0)


def header(c, number, title, subtitle):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 128, W, 128, fill=1, stroke=0)
    paragraph(c, "DAY 02 / AI PRODUCT SCOPING", 44, H - 23, W - 88, 11,
              colors.HexColor("#97DAD1"), True)
    paragraph(c, title, 44, H - 49, W - 88, 27, colors.white, True)
    paragraph(c, subtitle, 44, H - 94, W - 88, 12, colors.HexColor("#D2DEEA"))
    paragraph(c, "Hoàng Bảo Nguyên  |  2A202603384  |  07/11/2026", 44, 42,
              W - 180, 10, MUTED)
    paragraph(c, f"{number} / 2", W - 100, 42, 56, 11, MUTED, align=TA_CENTER)


def summary(c, left, right):
    c.setFillColor(colors.white)
    c.roundRect(44, 654, W - 88, 45, 9, fill=1, stroke=0)
    paragraph(c, left, 60, 687, 680, 14, NAVY, True)
    paragraph(c, right, 755, 684, W - 815, 11, ORANGE, True, align=TA_CENTER)


def cards(c, items):
    gap = 18
    card_w = (W - 88 - gap * 5) / 6
    positions = []
    for i, (title, actor, body, time_label, accent) in enumerate(items):
        x, y, height = 44 + i * (card_w + gap), 385, 245
        positions.append((x, card_w))
        c.setFillColor(colors.white)
        c.setStrokeColor(colors.HexColor("#D6E0E9"))
        c.setLineWidth(1)
        c.roundRect(x, y, card_w, height, 10, fill=1, stroke=1)
        c.setFillColor(accent)
        c.roundRect(x, y + height - 67, card_w, 67, 10, fill=1, stroke=0)
        c.rect(x, y + height - 67, card_w, 11, fill=1, stroke=0)
        paragraph(c, title, x + 12, y + height - 13, card_w - 24, 13,
                  colors.white, True, max_height=54)
        paragraph(c, actor, x + 12, y + height - 81, card_w - 24, 10,
                  MUTED, True, max_height=43)
        paragraph(c, body, x + 12, y + height - 130, card_w - 24, 11,
                  INK, max_height=78)
        paragraph(c, time_label, x + 12, y + 30, card_w - 24, 13,
                  accent, True, max_height=23)
        if i:
            prev_x, prev_w = positions[i - 1]
            arrow(c, prev_x + prev_w + 3, 505, x - 4, 505)
    return positions


def callout(c, text, x, y, width, height, fill, color=INK):
    c.setFillColor(colors.HexColor(fill))
    c.roundRect(x, y, width, height, 9, fill=1, stroke=0)
    paragraph(c, text, x + 16, y + height - 13, width - 32, 12,
              color, max_height=height - 22)


def build():
    output = ROOT / "04-workflow-diagram.pdf"
    c = canvas.Canvas(str(output), pagesize=(W, H))
    c.setTitle("Day 02 - Workflow Xanh SM - Hoàng Bảo Nguyên")
    c.setAuthor("Hoàng Bảo Nguyên - 2A202603384")

    header(c, 1, "Quy trình hiện tại: xử lý sự cố pin",
           "Current-state / 6 bước / workflow giả định để discovery; chưa đo tại doanh nghiệp")
    summary(c, "12 phút/case  |  B3 + B4 = 6 phút = 50% thời gian", "GIẢ ĐỊNH BASELINE")
    positions = cards(c, [
        ("B1 / Nhận tin", "ĐIỀU PHỐI VIÊN", "Tin nhắn/cuộc gọi → phiếu sự cố.<br/><b>H1:</b> Tài xế → điều phối.", "2 phút", BLUE),
        ("B2 / Xác minh", "NGƯỜI + DASHBOARD", "Mã xe/case → pin và độ mới dữ liệu.<br/><b>H2:</b> Dashboard → operator.", "2 phút", BLUE),
        ("B3 / Tra cứu", "ĐIỀU PHỐI VIÊN", "Pin, vị trí, trạm → phương án sơ bộ.<br/><b>BOTTLENECK:</b> chuyển công cụ.", "3 phút", ORANGE),
        ("B4 / Soạn nháp", "ĐIỀU PHỐI VIÊN", "Phương án → lời nhắn theo tình huống.<br/><b>BOTTLENECK:</b> viết lại thủ công.", "3 phút", ORANGE),
        ("B5 / Duyệt, gửi", "NGƯỜI CÓ THẨM QUYỀN", "Nháp → phản hồi được duyệt.<br/><b>H3:</b> Người duyệt → kênh tài xế.", "1 phút", TEAL),
        ("B6 / Ghi nhận", "ĐIỀU PHỐI VIÊN", "Phản hồi → nhật ký case.<br/><b>H4:</b> Điều phối → ca sau/đội xử lý.", "1 phút", BLUE),
    ])
    c.setDash(5, 4)
    bx, bw = positions[1]
    c.setStrokeColor(ORANGE)
    c.line(bx + bw / 2, 385, bx + bw / 2, 349)
    c.line(bx + bw / 2, 349, W / 2, 349)
    c.setDash()
    arrow(c, W / 2, 349, W / 2, 330, ORANGE)
    callout(c, "<b>Ngoại lệ tại B2/B3:</b> thiếu, cũ hoặc mâu thuẫn dữ liệu → hỏi lại tài xế / trưởng ca → quay lại xác minh. Chưa có thời gian chờ đo được; ghi riêng khi thu baseline.",
            265, 255, W - 530, 75, "#FFF0E5")
    callout(c, "<b>Phạm vi đo:</b> từ nhận sự cố tới hoàn tất duyệt, gửi và ghi nhận. Không bao gồm thời gian cứu hộ đến nơi. Sáu bước là tuyến thường lệ; không bỏ qua lượt hỏi lại khi đo thực tế.",
            44, 148, W - 88, 72, "#E8EFF6")
    paragraph(c, "Nguồn: giả thuyết workflow trong báo cáo cá nhân, mục 2. Handoff = điểm chuyển giao thông tin giữa người/hệ thống. Thời gian là giả định cần đo lại.",
              44, 112, W - 88, 10, MUTED)
    c.showPage()

    header(c, 2, "Quy trình tương lai: Rule + LLM + người duyệt",
           "Future-state / luồng cố định / LLM chỉ hỗ trợ nháp; mọi hành động do con người thực hiện")
    summary(c, "5 phút/case hợp lệ  |  20% fallback → mean dự kiến 6,5 phút", "MỤC TIÊU, CHƯA ĐO")
    positions = cards(c, [
        ("F1 / Nhận case", "NGƯỜI", "Tiếp nhận, xác thực mã case.<br/>Input của tài xế không phải telemetry tin cậy.", "1,5 phút", TEAL),
        ("F2 / Context", "ỨNG DỤNG / DATA", "Đọc pin, tuổi dữ liệu và trạm được phép.<br/>Repo dùng context mô phỏng.", "0,5 phút", BLUE),
        ("F3 / Rule", "KIỂM TRA CỐ ĐỊNH", "Kiểu dữ liệu, tuổi ≤300s, pin và điều kiện trạm → nhánh đề xuất.", "0,5 phút", BLUE),
        ("F4 / LLM nháp", "LLM + VALIDATOR", "Tạo tag + JSON; kiểm action, approval và id trạm.<br/>Không có tool thực thi.", "0,2 phút", PURPLE),
        ("F5 / HITL", "ĐIỀU PHỐI VIÊN", "Đọc căn cứ, sửa ngữ nghĩa, duyệt hoặc từ chối.<br/>Approval luôn bắt buộc.", "1,5 phút", TEAL),
        ("F6 / Thực hiện", "CON NGƯỜI + LOG", "Người gửi/điều phối qua hệ thống hiện hành; lưu log và kết quả.", "0,8 phút", TEAL),
    ])
    c.setStrokeColor(ORANGE)
    c.setDash(5, 4)
    for index in (1, 2, 3):
        x, width = positions[index]
        c.line(x + width / 2, 385, x + width / 2, 350)
    c.line(positions[1][0] + positions[1][1] / 2, 350,
           positions[3][0] + positions[3][1] / 2, 350)
    c.setDash()
    arrow(c, W / 2, 350, W / 2, 331, ORANGE)
    callout(c, "<b>Fallback:</b> context thiếu/cũ, API lỗi hoặc output vi phạm → dùng thông báo mẫu, điều phối viên xác minh và xử lý thủ công. Giữ raw failure trong evidence; không tính fallback là model pass.",
            245, 255, W - 490, 76, "#FFF0E5")
    callout(c, "<b>Boundary:</b> pin &lt;5% → đề xuất cứu hộ có duyệt; dữ liệu không hợp lệ → chuyển người. Ngưỡng 5%, 5 km và 300 giây là policy lab, không xác nhận xe di chuyển an toàn. Prototype không gửi tin hoặc gọi cứu hộ thật.",
            44, 147, W - 88, 74, "#E8EFF6")
    paragraph(c, "Màu xanh dương: rule/data  |  Tím: LLM  |  Xanh lá: con người  |  Cam: bottleneck/ngoại lệ. Quyết định: GO technical synthetic; NOT YET pilot thật.",
              44, 111, W - 88, 10, MUTED)
    c.save()
    print(str(output))


if __name__ == "__main__":
    build()
