"""
CMS Platform Selection Scorecard Generator
───────────────────────────────────────────
Usage
  1. Fill in CLIENT_NAME, PLATFORMS, and CATEGORIES below.
  2. Run from the project root:
       source /tmp/xlsx_env/bin/activate
       python3 skills/cms-platform-selection/scripts/generate_scorecard.py

Output
  deliverables/{CLIENT_NAME}-CMS-Platform-Selection-Scorecard.xlsx
"""

import shutil
import datetime
from copy import copy
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter

# ══════════════════════════════════════════════════════════════════════════════
# AGENT: fill in the three variables below, then run the script.
# ══════════════════════════════════════════════════════════════════════════════

CLIENT_NAME = "ClientName"   # used in the output filename

PLATFORMS = [
    "Platform 1",            # column D/E/F
    "Platform 2",            # column G/H/I
    "Platform 3",            # column J/K/L
]

# Each category is (category_name, [requirements])
# Each requirement is an 8-tuple:
#   (label, weight, p1_score, p1_comment, p2_score, p2_comment, p3_score, p3_comment)
# Scores: 3 = Strong | 2 = Partial | 1 = Weak | 0 = N/A (hard blocker)

CATEGORIES = [
    ("1. Architecture & Core Fit", [
        (
            "Headless / API-first architecture",
            5,
            3, "Strong API-first flexibility.",
            3, "Headless-first with visual editing layer.",
            3, "Fully headless, API-driven SaaS.",
        ),
        # Add more requirements here …
    ]),
    ("2. Editor Experience", [
        (
            "Visual editor / in-context live preview",
            4,
            2, "Preview requires developer setup.",
            3, "WYSIWYG Visual Editor is a flagship capability.",
            3, "Visual Builder enables in-context editing.",
        ),
        # Add more requirements here …
    ]),
    # Add more categories here …
]

# ══════════════════════════════════════════════════════════════════════════════
# Generator — no edits needed below this line.
# ══════════════════════════════════════════════════════════════════════════════

TEMPLATE = Path("templates/cms-platform-selection/CMS-selection-scorecard-template.xlsx")
OUTPUT   = Path(f"deliverables/{CLIENT_NAME}-CMS-Platform-Selection-Scorecard.xlsx")


def _freeze(cell):
    """Snapshot all style attributes of a cell into a plain dict."""
    return {
        "font":   copy(cell.font),
        "fill":   copy(cell.fill),
        "border": copy(cell.border),
        "align":  copy(cell.alignment),
        "numfmt": cell.number_format,
    }


def _apply(cell, style: dict):
    cell.font          = copy(style["font"])
    cell.fill          = copy(style["fill"])
    cell.border        = copy(style["border"])
    cell.alignment     = copy(style["align"])
    cell.number_format = style["numfmt"]


def generate():
    assert TEMPLATE.exists(), f"Template not found: {TEMPLATE}"
    assert len(PLATFORMS) == 3, "Exactly 3 platform names required."
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(TEMPLATE, OUTPUT)

    wb = openpyxl.load_workbook(OUTPUT)
    ws = wb["CMS Scorecard"]

    # ── snapshot style references from the template before clearing ──────────
    S = {
        "cat_hdr":   _freeze(ws["A10"]),   # dark category header, col A
        "cat_hdr_c": _freeze(ws["C10"]),   # Weight column header
        "cat_hdr_d": _freeze(ws["D10"]),   # Score / comment column headers
        "req_b":     _freeze(ws["B11"]),   # requirement label
        "req_c":     _freeze(ws["C11"]),   # weight (editable)
        "req_d":     _freeze(ws["D11"]),   # score cell (grey fill)
        "req_e":     _freeze(ws["E11"]),   # weighted formula cell
        "req_f":     _freeze(ws["F11"]),   # comment cell (grey fill)
        "total_b":   _freeze(ws["B15"]),   # TOTAL label
        "total_d":   _freeze(ws["D15"]),   # TOTAL score
        "total_e":   _freeze(ws["E15"]),   # TOTAL weighted score
        "grand_b":   _freeze(ws["B65"]),
        "grand_d":   _freeze(ws["D65"]),
        "grand_e":   _freeze(ws["E65"]),
        "max_b":     _freeze(ws["B66"]),
        "max_d":     _freeze(ws["D66"]),
        "pct_b":     _freeze(ws["B67"]),
        "pct_d":     _freeze(ws["D67"]),
        "pct_e":     _freeze(ws["E67"]),
    }

    # ── unmerge and clear rows 10+ ────────────────────────────────────────────
    for merge in list(ws.merged_cells.ranges):
        if merge.min_row >= 10:
            ws.unmerge_cells(str(merge))
    for r in range(10, ws.max_row + 1):
        for c in range(1, 13):
            ws.cell(r, c).value = None

    # ── update date (B3 in template — part of merged B3:C3) ──────────────────
    try:
        ws["B3"] = datetime.date.today()
    except Exception:
        pass

    # ── update platform names in header row 9 ────────────────────────────────
    for idx, (name, col) in enumerate(zip(PLATFORMS, [4, 7, 10])):
        ws.cell(9, col).value = name

    # ── write categories and requirements ─────────────────────────────────────
    row = 10
    total_rows: list[int] = []

    for cat_name, reqs in CATEGORIES:
        # Category header row
        _apply(ws.cell(row, 1, cat_name), S["cat_hdr"])
        _apply(ws.cell(row, 2, None),     S["cat_hdr"])
        _apply(ws.cell(row, 3, "Weight (1-5)"), S["cat_hdr_c"])
        for col in [4, 7, 10]:
            _apply(ws.cell(row, col,   "Score (0-3)"),            S["cat_hdr_d"])
            _apply(ws.cell(row, col+1, "Weighted score"),         S["cat_hdr_d"])
            _apply(ws.cell(row, col+2, "Comments / justification"), S["cat_hdr_d"])
        row += 1
        req_start = row

        for label, weight, s1, c1, s2, c2, s3, c3 in reqs:
            ws.cell(row, 1).value = None
            _apply(ws.cell(row, 2, label),  S["req_b"])
            _apply(ws.cell(row, 3, weight), S["req_c"])

            for score, comment, sc_col, ws_col, cm_col in [
                (s1, c1,  4,  5,  6),
                (s2, c2,  7,  8,  9),
                (s3, c3, 10, 11, 12),
            ]:
                _apply(ws.cell(row, sc_col, score), S["req_d"])
                _apply(ws.cell(row, ws_col,
                               f"=C{row}*{get_column_letter(sc_col)}{row}"), S["req_e"])
                _apply(ws.cell(row, cm_col, comment), S["req_f"])
            row += 1

        req_end = row - 1

        # TOTAL row
        total_rows.append(row)
        ws.cell(row, 1).value = None
        _apply(ws.cell(row, 2, "TOTAL"), S["total_b"])
        ws.cell(row, 3).value = None
        for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
            cl = get_column_letter
            _apply(ws.cell(row, sc_col,
                           f"=SUM({cl(sc_col)}{req_start}:{cl(sc_col)}{req_end})"),
                   S["total_d"])
            _apply(ws.cell(row, ws_col,
                           f"=SUM({cl(ws_col)}{req_start}:{cl(ws_col)}{req_end})"),
                   S["total_e"])
        row += 2   # blank gap between categories

    # ── summary section ───────────────────────────────────────────────────────
    # Score column headers
    for col, hdr in [(4, "Score"), (5, "Weighted score"),
                     (7, "Score"), (8, "Weighted score"),
                     (10, "Score"), (11, "Weighted score")]:
        c = ws.cell(row, col, hdr)
        c.font = Font(bold=True)
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    row += 1

    grand_row = row
    _apply(ws.cell(row, 2, "GRAND TOTAL SCORE"), S["grand_b"])
    ws.cell(row, 3).value = None
    for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
        cl = get_column_letter
        _apply(ws.cell(row, sc_col,
                       "=" + "+".join(f"{cl(sc_col)}{r}" for r in total_rows)),
               S["grand_d"])
        _apply(ws.cell(row, ws_col,
                       "=" + "+".join(f"{cl(ws_col)}{r}" for r in total_rows)),
               S["grand_e"])
    row += 1

    max_row = row
    total_reqs = sum(len(r) for _, r in CATEGORIES)
    _apply(ws.cell(row, 2, "Max total score"), S["max_b"])
    ws.cell(row, 3).value = None
    for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
        cl = get_column_letter
        _apply(ws.cell(row, sc_col, f"={total_reqs}*3"),     S["max_d"])
        _apply(ws.cell(row, ws_col, f"=5*{cl(sc_col)}{row}"), S["max_d"])
    row += 1

    _apply(ws.cell(row, 2, "%"), S["pct_b"])
    ws.cell(row, 3).value = None
    for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
        cl = get_column_letter
        pct_sc = ws.cell(row, sc_col,
                         f"={cl(sc_col)}{grand_row}/{cl(sc_col)}{max_row}")
        _apply(pct_sc, S["pct_d"]); pct_sc.number_format = "0%"
        pct_ws = ws.cell(row, ws_col,
                         f"={cl(ws_col)}{grand_row}/{cl(ws_col)}{max_row}")
        _apply(pct_ws, S["pct_e"]); pct_ws.number_format = "0%"

    # ── formatting ────────────────────────────────────────────────────────────
    wrap_top_left = Alignment(wrap_text=True, vertical="top", horizontal="left")
    for r in range(10, row + 1):
        ws.row_dimensions[r].height = 55
        for c in range(1, 13):
            ws.cell(r, c).alignment = copy(wrap_top_left)

    wb.save(OUTPUT)
    print(f"✓  {OUTPUT}")
    print(f"   {total_reqs} requirements · {len(CATEGORIES)} categories · {len(PLATFORMS)} platforms")
    print(f"   TOTAL rows : {total_rows}")
    print(f"   Grand total: row {grand_row} · Max score: row {max_row}")


if __name__ == "__main__":
    generate()
