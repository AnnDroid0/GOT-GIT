#!/usr/bin/env python3
"""Build the one-page git cheat sheet PDF from cheatsheet-source.md.

Usage (from this folder):
    pip install reportlab
    python3 build_cheatsheet.py
    python3 build_cheatsheet.py my-source.md my-output.pdf   # optional names

To change the sheet, edit cheatsheet-source.md (plain markdown that also
renders on GitHub) and rerun this script. See the comment at the top of the
source file for the editing rules.
"""
import re
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether,
                                PageTemplate, Paragraph, Spacer, Table,
                                TableStyle)

SRC = sys.argv[1] if len(sys.argv) > 1 else "cheatsheet-source.md"
OUT = sys.argv[2] if len(sys.argv) > 2 else "git-cheatsheet.pdf"

BLUE = colors.HexColor("#1f3a5f")
RED = colors.HexColor("#9b2226")
STRIPE = colors.HexColor("#eef2f7")
NOTE = colors.HexColor("#444444")

W, H = landscape(letter)
M, GAP, COLS = 24, 10, 3
BANNER_H = 26
colw = (W - 2 * M - GAP * (COLS - 1)) / COLS
top = H - M - BANNER_H - 8


def parse(path):
    """Return (title, subtitle, sections). Each section is a dict."""
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    title, subtitle, sections, cur = "GIT CHEAT SHEET", "", [], None
    table_lines_seen = 0
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            head = line[3:].strip()
            red = head.endswith("{red}")
            head = head.replace("{red}", "").strip()
            cur = {"title": head, "red": red, "rows": [], "tip": ""}
            sections.append(cur)
            table_lines_seen = 0
        elif line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("> "):
            if cur is None:
                subtitle = line[2:].strip()
            else:
                cur["tip"] = line[2:].strip()
        elif line.startswith("|") and cur is not None:
            table_lines_seen += 1
            if table_lines_seen <= 2:  # header and |-|-| separator
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2:
                cur["rows"].append((cells[0], cells[1]))
    return title, subtitle, sections


def clean(s):
    s = s.replace("`", "")
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


head_style = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8.6,
                            textColor=colors.white, leading=10)
cmd_style = ParagraphStyle("c", fontName="Courier-Bold", fontSize=6.7,
                           leading=8)
txt_style = ParagraphStyle("t", fontName="Helvetica", fontSize=6.9, leading=8)
note_style = ParagraphStyle("n", fontName="Helvetica-Oblique", fontSize=6.6,
                            leading=8, textColor=NOTE)


def build_section(sec):
    color = RED if sec["red"] else BLUE
    data = [[Paragraph(clean(sec["title"]).upper(), head_style), ""]]
    for a, b in sec["rows"]:
        data.append([Paragraph(clean(a), cmd_style),
                     Paragraph(clean(b), txt_style)])
    t = Table(data, colWidths=[colw * 0.52, colw * 0.48])
    t.setStyle(TableStyle([
        ("SPAN", (0, 0), (1, 0)),
        ("BACKGROUND", (0, 0), (1, 0), color),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, STRIPE]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
        ("BOX", (0, 0), (-1, -1), 0.5, color),
    ]))
    items = [t]
    if sec["tip"]:
        items.append(Paragraph(clean(sec["tip"]), note_style))
    items.append(Spacer(1, 5))
    return KeepTogether(items)


def main():
    title, subtitle, sections = parse(SRC)

    def banner(c, d):
        c.saveState()
        c.setFillColor(BLUE)
        c.rect(M, H - M - BANNER_H, W - 2 * M, BANNER_H, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(M + 8, H - M - 18, title.upper())
        c.setFont("Helvetica", 9)
        c.drawRightString(W - M - 8, H - M - 17, subtitle)
        c.restoreState()

    doc = BaseDocTemplate(OUT, pagesize=landscape(letter), leftMargin=M,
                          rightMargin=M, topMargin=M, bottomMargin=M,
                          title=title)
    frames = [Frame(M + i * (colw + GAP), M, colw, top - M, leftPadding=0,
                    rightPadding=0, topPadding=0, bottomPadding=0)
              for i in range(COLS)]
    doc.addPageTemplates([PageTemplate(id="p", frames=frames, onPage=banner)])
    doc.build([build_section(s) for s in sections])

    if doc.page > 1:
        print(f"WARNING: the sheet runs to {doc.page} pages. Shorten a note "
              f"or remove a row in {SRC}, then rebuild.")
        sys.exit(1)
    print(f"Built {OUT}: 1 page, {len(sections)} boxes.")


if __name__ == "__main__":
    main()
