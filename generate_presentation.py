#!/usr/bin/env python3
"""
Generate the Release 10.9 Retrospective presentation (PPTX).
Run: python generate_presentation.py
Output: retro_109_presentation.pptx (26 slides, dark theme)
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

# Colors
DARK_BG = RGBColor(0x1B, 0x1B, 0x2F)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT_BLUE = RGBColor(0x4E, 0xC5, 0xF1)
ACCENT_GREEN = RGBColor(0x4E, 0xC9, 0x6F)
ACCENT_RED = RGBColor(0xE7, 0x4C, 0x3C)
ACCENT_ORANGE = RGBColor(0xF3, 0x9C, 0x12)
ACCENT_YELLOW = RGBColor(0xF1, 0xC4, 0x0F)
LIGHT_GRAY = RGBColor(0xBD, 0xBD, 0xBD)


def add_dark_bg(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BG


def add_title_slide(title, subtitle=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_dark_bg(slide)
    txBox = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(11), Inches(2))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(20)
        p2.font.color.rgb = LIGHT_GRAY
        p2.alignment = PP_ALIGN.CENTER
    return slide


def add_section_slide(title):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_dark_bg(slide)
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(3.3), Inches(0.15), Inches(0.9))
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT_BLUE
    shape.line.fill.background()
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(3), Inches(12), Inches(1.5))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    return slide


def add_content_slide(title, content_lines):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_dark_bg(slide)
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12), Inches(0.8))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    txBox2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(12.3), Inches(5.8))
    tf2 = txBox2.text_frame
    tf2.word_wrap = True
    for i, line in enumerate(content_lines):
        if i == 0:
            p = tf2.paragraphs[0]
        else:
            p = tf2.add_paragraph()
        if isinstance(line, tuple):
            text, size, color, bold = line
        else:
            text, size, color, bold = line, 18, WHITE, False
        p.text = text
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.bold = bold
        p.space_after = Pt(6)
    return slide


def add_table_slide(title, headers, rows, col_widths=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_dark_bg(slide)
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12), Inches(0.7))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    num_rows = len(rows) + 1
    num_cols = len(headers)
    left = Inches(0.4)
    top = Inches(1.1)
    width = Inches(12.5)
    height = Inches(0.4) * num_rows
    table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
    table = table_shape.table
    if col_widths:
        for i, w in enumerate(col_widths):
            table.columns[i].width = Inches(w)
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = WHITE
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0x2C, 0x3E, 0x50)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = table.cell(r + 1, c)
            cell.text = str(val)
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.font.color.rgb = WHITE
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(0x22, 0x22, 0x3A) if r % 2 == 0 else RGBColor(0x1B, 0x1B, 0x2F)
    return slide


# ===== SLIDES =====

# 1: Title
add_title_slide(
    "Release 10.9 Retrospective",
    "RCA & Action Items — Dana, Shlomi, Rajeev squads\nTimeline: Sprint 0 (Sep 30) → FF (Jan 26) → CF (Feb 17) → GA (May 13)"
)

# 2: KPI Overview
add_table_slide(
    "KPI Comparison: 10.8 → 10.9",
    ["Metric", "KPI", "10.8", "10.9", "Δ", "Trend"],
    [
        ["Breached FF (stories)", "0", "37", "25", "-12", "✅ Improved (-32%)"],
        ["Breached CF (stories)", "0", "23", "36", "+13", "❌ Worse (+57%)"],
        ["Breached CF (bugs)", "0", "4", "6", "+2", "❌ Worse"],
        ["Regression total", "<10", "50", "152", "+102", "❌ Worse (+204%)"],
        ["Regression in hardening", "<4", "17", "60", "+43", "❌ Worse (+253%)"],
        ["Automation detection", "+20%", "32%", "TBD", "—", "❌ Dropped"],
    ],
    col_widths=[3.5, 1.0, 1.0, 1.0, 1.0, 4.0]
)

# 3: Per-GM Summary
add_table_slide(
    "Per-GM Breakdown",
    ["Metric", "Dana 10.8→10.9", "Shlomi 10.8→10.9", "Rajeev 10.8→10.9"],
    [
        ["Breached FF", "7→6 ✅", "0→8 ❌", "30→11 ✅"],
        ["Breached CF Stories", "6→2 ✅", "3→9 ❌", "14→25 ❌"],
        ["Breached CF Bugs", "2→2 ➡️", "2→2 ➡️", "0→2 ❌"],
        ["Regression total", "19→95 ❌", "4→27 ❌", "27→30 ❌"],
        ["Regression hardening", "11→37 ❌", "1→17 ❌", "5→6 ➡️"],
        ["Verdict", "FF/CF improved\nRegressions 5×", "All worse", "FF great\nCF doubled"],
    ],
    col_widths=[3.0, 3.2, 3.2, 3.2]
)

# 4: What Improved
add_content_slide("✅ Improvements 10.8 → 10.9", [
    ("FF discipline improved: 37 → 25 breaches (-32%)", 18, ACCENT_GREEN, False),
    ("Dana CF breach: 6 → 2 stories at Code Freeze", 18, ACCENT_GREEN, False),
    ("Rajeev FF significantly improved: 30 → 11", 18, ACCENT_GREEN, False),
    ("Dana FF improved: 7 → 6", 18, ACCENT_GREEN, False),
    ("Rajeev regressions nearly stable: 27 → 30", 18, ACCENT_GREEN, False),
    ("", 12, WHITE, False),
    ("Positive pattern: upgrade testing during development (Rajeev)", 16, LIGHT_GRAY, False),
])

# 5: Section - RCA
add_section_slide("Root Cause Analysis")

# 6: Regression RCA
add_table_slide(
    "Regression Total: 50 → 152 (+204%) — Top Contributors",
    ["Squad (GM)", "10.8", "10.9", "Δ", "Root Cause"],
    [
        ["Nils (Dana)", "16", "60", "+44", "React Migration — all new bugs = regressions"],
        ["GreenBoat (Rajeev)", "15", "22", "+7", "Upgrade scenarios, EF cache, code conflicts"],
        ["Cloud Compliance (Dana)", "—", "19", "—", "Security/compliance bugs, 0 by automation"],
        ["Driver (Shlomi)", "1", "11", "+10", "VME/VAIO — low quality dev testing"],
        ["VRA (Shlomi)", "3", "10", "+7", "Scale issues at large setups"],
        ["Azure (Dana)", "3", "8", "+5", "GPv2 performance, recovery stuck"],
        ["Apex (Rajeev)", "6", "8", "+2", "Secret Centralization + late testing"],
    ],
    col_widths=[2.5, 0.8, 0.8, 0.8, 7.5]
)

# 7: FF & CF Breach RCA
add_content_slide("FF & CF Breach Root Causes", [
    ("FF Breaches (25 total):", 20, ACCENT_ORANGE, True),
    ("  • Cyber Resilience (7): Late requirements — design approved end Sprint 4", 16, WHITE, False),
    ("  • Apex Legends (7): Stories in RFT but QA bandwidth limited", 16, WHITE, False),
    ("  • GreenBoat (4): Dependencies on Linux migration + waiver", 16, WHITE, False),
    ("  • Nils (2), Azure (2), AI Agents (2), Driver (1)", 16, WHITE, False),
    ("", 10, WHITE, False),
    ("CF Breaches (36 stories):", 20, ACCENT_RED, True),
    ("  • GreenBoat (13): Public Cloud test setup not ready", 16, WHITE, False),
    ("  • Apex Legends (12): Testing started late, stories stuck in QA", 16, WHITE, False),
    ("  • Mavka (4), Cyber Resilience (4): Late start", 16, WHITE, False),
    ("  • AI Agents (2), Driver (1)", 16, WHITE, False),
])

# 8: Automation drop
add_content_slide("Automation Detection Rate — Dropped", [
    ("Most concerning metric — target is +20% improvement, we went backwards", 18, ACCENT_RED, True),
    ("", 10, WHITE, False),
    ("Why?", 20, ACCENT_ORANGE, True),
    ("  • New bugs concentrated in React (Nils=60) and VME (Driver=11)", 16, WHITE, False),
    ("  • These areas have LOW automation coverage", 16, WHITE, False),
    ("  • React has Cypress but insufficient for complex scenarios", 16, WHITE, False),
    ("  • VME/Driver has minimal automation — 'N/A' per Shlomi", 16, WHITE, False),
    ("  • Cloud Compliance (19 regressions): 0/19 found by automation", 16, WHITE, False),
    ("", 10, WHITE, False),
    ("152 regressions total — vast majority in low-automation areas", 16, LIGHT_GRAY, False),
])

# 9: Section - RFT
add_section_slide("QA-Dev Interface:\nReady For Testing Backlog")

# 10: RFT Growth
add_table_slide(
    "RFT Backlog Growth: 75 → 196 items (+161%)",
    ["Milestone", "Items in RFT", "Notes"],
    [
        ["10.9 Sprint 1", "75", "Baseline"],
        ["10.9 Sprint 4", "84", "+12%"],
        ["10.9 Feature Freeze", "87", "Stable"],
        ["10.9 Code Freeze", "45", "Consumed during hardening"],
        ["10.10 Sprint 1", "94", "Immediately refilled"],
        ["10.10 Sprint 2", "169", "⚠️ Spike"],
        ["Today", "196", "❌ +161% from baseline"],
    ],
    col_widths=[3.5, 2.5, 6.5]
)

# 11: RFT per squad
add_content_slide("RFT Backlog: Per Squad & Aging", [
    ("Current: 196 items. 75% older than 30 days. 55 items > 3 months.", 18, ACCENT_RED, True),
    ("", 8, WHITE, False),
    ("Top squads:", 18, ACCENT_BLUE, True),
    ("  • Nils (Dana): 50 items, avg 71 days old", 16, WHITE, False),
    ("  • Opus (Dana): 31 items, avg 57 days old", 16, WHITE, False),
    ("  • Azure (Dana): 25 items, avg 97 days old ⚠️", 16, ACCENT_ORANGE, False),
    ("  • Apex Legends (Rajeev): 16 items, avg 90 days old", 16, WHITE, False),
    ("  • GreenBoat (Rajeev): items in queue", 16, WHITE, False),
    ("", 8, WHITE, False),
    ("10.8 FF vs 10.9 FF: RFT grew from 39 → 64 items (+64%)", 16, LIGHT_GRAY, False),
    ("Stuck > 3 weeks: doubled from 3 → 7", 16, LIGHT_GRAY, False),
])

# 12: Section - Lifecycle
add_section_slide("Epic & Story Lifecycle\nSLA Analysis")

# 13: Story Lifecycle per GM
add_table_slide(
    "Story Active Cycle Time (In Progress → Completed)",
    ["Phase", "All (n=61)", "Dana", "Shlomi", "Rajeev ⚠️"],
    [
        ["Dev Time (IP → RFT)", "27d avg / 12d med", "7d / 5d", "11d / 7d", "42d / 15d"],
        ["QA Queue (RFT → Testing)", "25d avg / 14d med", "15d / 19d", "10d / 6d", "44d / 29d ⚠️"],
        ["QA Execution (Testing → Done)", "15d avg / 3d med", "2d / 0d", "6d / 2d", "33d / 28d ⚠️"],
        ["Total Active Cycle", "56d avg / 27d med", "18d / 11d ✅", "24d / 21d ✅", "90d / 74d ❌"],
    ],
    col_widths=[3.5, 2.5, 2.0, 2.0, 2.5]
)

# 14: Story lifecycle per squad
add_table_slide(
    "Story Lifecycle — Per Squad",
    ["Squad (GM)", "Total Active (avg/med)", "QA Queue (avg/med)", "Concern"],
    [
        ["GreenBoat (Rajeev)", "95d / 80d", "45d / 29d", "⚠️ Longest cycle + QA queue"],
        ["Apex Legends (Rajeev)", "83d / 27d", "41d / 26d", "⚠️ High variability"],
        ["Cyber Resilience (Shlomi)", "24d / 24d", "11d / 6d", "✅ Healthy"],
        ["Cloud Azure (Dana)", "19d / 19d", "16d / 19d", "✅ Healthy"],
    ],
    col_widths=[3.5, 3.0, 3.0, 3.5]
)

# 15: Epic phases
add_content_slide("Epic Lifecycle Phases", [
    ("Workflow: New → Ready For Dev → In Development → Ready To Ship", 16, LIGHT_GRAY, False),
    ("", 8, WHITE, False),
    ("FR Phase (New → Ready For Development):", 20, ACCENT_BLUE, True),
    ("  Overall: avg 71d, median 21d (n=11)", 16, WHITE, False),
    ("  Shlomi: avg 94d — late requirement injection", 16, ACCENT_ORANGE, False),
    ("  Rajeev: avg 57d, median 35d", 16, WHITE, False),
    ("", 8, WHITE, False),
    ("Planning Wait (Ready For Dev → In Development):", 20, ACCENT_BLUE, True),
    ("  Overall: avg 43d, median 30d (n=10)", 16, WHITE, False),
    ("  Rajeev: avg 50d — epics sit idle ~7 weeks after FR done", 16, ACCENT_ORANGE, False),
    ("  Shlomi: avg 26d — reasonable", 16, WHITE, False),
    ("", 8, WHITE, False),
    ("Design stories (once started): avg 31d — not a bottleneck ✅", 16, ACCENT_GREEN, False),
])

# 16: Key findings
add_content_slide("Key Findings: Where Does Time Go?", [
    ("1. QA Queue is #1 time sink for Rajeev", 20, ACCENT_RED, True),
    ("   44 days avg waiting in RFT. GreenBoat=45d, Apex=41d", 16, WHITE, False),
    ("", 6, WHITE, False),
    ("2. Rajeev's cycle is 4-5× longer than Dana/Shlomi", 20, ACCENT_RED, True),
    ("   90d vs 18-24d. Long dev + long QA queue + long QA execution", 16, WHITE, False),
    ("", 6, WHITE, False),
    ("3. FR Phase avg 71 days at epic level", 20, ACCENT_ORANGE, True),
    ("   Shlomi's epics avg 94d. Requirements not locked early enough", 16, WHITE, False),
    ("", 6, WHITE, False),
    ("4. Planning idle after FR: 43 days", 20, ACCENT_ORANGE, True),
    ("   Epics ready for dev but nobody picks them up for 6 weeks", 16, WHITE, False),
    ("", 6, WHITE, False),
    ("5. Dana & Shlomi story cycles are healthy (18-24d)", 18, ACCENT_GREEN, True),
])

# 17: Section - 10.8 cross-ref
add_section_slide("10.8 Retro Cross-Reference")

# 18: 10.8 findings
add_table_slide(
    "10.8 Findings: What Was Actually Addressed?",
    ["10.8 Finding", "10.9 Result", "Verdict"],
    [
        ["Don't enable FE tweaks late", "Same issue, Nils 16→60", "❌ NOT ADDRESSED"],
        ["React side-by-side comparison", "Not done", "❌ NOT ADDRESSED"],
        ["Increase Cypress coverage", "Rate dropped significantly", "❌ NOT ADDRESSED"],
        ["Clarify cross-team ownership", "Same GB/AWS blame", "❌ NOT ADDRESSED"],
        ["Upgrade test during dev", "Rajeev regressions FLAT", "✅ ADDRESSED"],
        ["Scale setups lacking", "Still not ready", "❌ NOT ADDRESSED"],
        ["ZIC timeline different", "Under discussion", "⏳ IN PROGRESS"],
        ["Enhance ZIC quality", "Cyber FF breach +7", "❌ NOT ADDRESSED"],
    ],
    col_widths=[4.0, 4.0, 4.5]
)

# 19: Score
add_content_slide("10.8 → 10.9 Improvement Score", [
    ("", 10, WHITE, False),
    ("1 / 8  improvements implemented", 36, ACCENT_RED, True),
    ("", 10, WHITE, False),
    ("1 / 8  in progress", 28, ACCENT_YELLOW, False),
    ("", 10, WHITE, False),
    ("6 / 8  not addressed", 28, ACCENT_RED, False),
    ("", 20, WHITE, False),
    ("We must break this pattern in 10.10", 20, WHITE, True),
])

# 20: Section - Action Items
add_section_slide("Action Items")

# 21: Dana actions
add_content_slide("Dana Mittelman — Priority: REGRESSION (95 bugs)", [
    ("D1: Enforce tweak activation policy", 18, WHITE, True),
    ("    No FE tweak after Sprint 5. Dev+QA sign-off required.", 14, LIGHT_GRAY, False),
    ("    Target: Zero regressions from late-activated tweaks", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("D2: React Migration quality gate", 18, WHITE, True),
    ("    Side-by-side visual comparison with AngularJS before merge", 14, LIGHT_GRAY, False),
    ("    Target: Nils regressions < 20 (down from 60)", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("D3: Cypress coverage plan for React", 18, WHITE, True),
    ("    Top 5 high-traffic pages covered by Sprint 3", 14, LIGHT_GRAY, False),
    ("    Target: Automation detection > 25% for Nils bugs", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("D4: Decouple Linux Migration tool from RC", 18, WHITE, True),
    ("    Target: Linux migration regressions moved to pre-CF", 14, ACCENT_GREEN, False),
])

# 22: Shlomi actions
add_content_slide("Shlomi Apel — Priority: ALL METRICS REGRESSED", [
    ("S1: Driver squad — mandatory dev self-testing checklist", 18, WHITE, True),
    ("    5 basic scenarios per feature before 'Ready for Testing'", 14, LIGHT_GRAY, False),
    ("    Target: Driver regressions < 4 (down from 11)", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("S2: HV testing setup always-available policy", 18, WHITE, True),
    ("    Target: Zero CF breaches from setup unavailability", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("S3: Scale testing capacity — escalate to VP/Infra", 18, WHITE, True),
    ("    Target: Scale tests parallel to dev (not sequential)", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("S4: Cyber Resilience — requirements locked by Sprint 2", 18, WHITE, True),
    ("    Target: Zero FF breaches from late requirements", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("S5: VRA scale checkpoint at Sprint 4", 18, WHITE, True),
    ("    Target: VRA P1 scale regressions = 0", 14, ACCENT_GREEN, False),
])

# 23: Rajeev actions
add_content_slide("Rajeev Srivastav — Priority: CF BREACH + QA QUEUE", [
    ("R1: GreenBoat — stabilize test env BEFORE Sprint 5", 18, WHITE, True),
    ("    If not ready by Sprint 5, descope dependent features", 14, LIGHT_GRAY, False),
    ("    Target: GB CF breach < 5 (down from 13)", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("R2: Cross-team impact ownership contract", 18, WHITE, True),
    ("    Signed ownership doc at design phase for cross-team changes", 14, LIGHT_GRAY, False),
    ("    Target: Zero cross-team blame escalations", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("R3: Apex Legends — QA bandwidth reservation", 18, WHITE, True),
    ("    Pre-allocate QA capacity in Sprint 5-6", 14, LIGHT_GRAY, False),
    ("    Target: Zero FF breaches from 'ready but not tested'", 14, ACCENT_GREEN, False),
    ("", 6, WHITE, False),
    ("R4: Upgrade regression gate in CI", 18, WHITE, True),
    ("    Target: Upgrade regressions < 3", 14, ACCENT_GREEN, False),
])

# 24: Org-level actions
add_content_slide("Org-Level Actions (Sandra)", [
    ("O1: Automation investment plan", 18, WHITE, True),
    ("    Dedicated automation sprint per GM. Target: > 25% rate", 14, LIGHT_GRAY, False),
    ("", 6, WHITE, False),
    ("O2: Tweak activation = formal release milestone", 18, WHITE, True),
    ("    Jira workflow step by Sprint 5. Measurable.", 14, LIGHT_GRAY, False),
    ("", 6, WHITE, False),
    ("O3: ZIC timeline decision", 18, WHITE, True),
    ("    Same FF/CF dates or different milestones? Decide now.", 14, LIGHT_GRAY, False),
    ("", 6, WHITE, False),
    ("O4: Mid-release regression checkpoint (Sprint 4)", 18, WHITE, True),
    ("    If any squad > 5 regressions by Sprint 4 → remediation plan", 14, LIGHT_GRAY, False),
    ("", 6, WHITE, False),
    ("L1: RFT WIP limit per squad (max 15 items)", 18, WHITE, True),
    ("    Target: RFT backlog < 100 at FF (down from 196)", 14, LIGHT_GRAY, False),
    ("", 6, WHITE, False),
    ("L5: Rajeev QA queue SLA: max 14 days in RFT", 18, WHITE, True),
    ("    Current: 44d avg. Investigate QA capacity gap.", 14, LIGHT_GRAY, False),
])

# 25: Jira Links (with clickable hyperlinks)
import urllib.parse

def jira_squad_reg_url(squad):
    jql = f'"Owning Team/Squad[Group Picker (single group)]" = "{squad}" AND affectedVersion = 10.9 AND "Regression?[Dropdown]" = Yes AND status not in (Obsolete)'
    return f"https://zerto.atlassian.net/issues/?jql={urllib.parse.quote(jql)}"

def add_links_slide():
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_dark_bg(slide)
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12), Inches(0.7))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Jira Links — Click to Verify"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    txBox2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.0), Inches(12.3), Inches(6.0))
    tf2 = txBox2.text_frame
    tf2.word_wrap = True

    links = [
        ("Filters:", None, True),
        ("  10.9 Dashboard", "https://zerto.atlassian.net/jira/dashboards/15285"),
        ("  FF Breach (25 stories)", "https://zerto.atlassian.net/issues/?filter=21636"),
        ("  CF Breach Stories (36)", "https://zerto.atlassian.net/issues/?filter=21637"),
        ("  CF Breach Bugs (6)", "https://zerto.atlassian.net/issues/?filter=21638"),
        ("", None),
        ("Regressions per Squad:", None, True),
        ("  Nils — 60 regressions", jira_squad_reg_url("Squad - Eng - Nils")),
        ("  GreenBoat — 22 regressions", jira_squad_reg_url("Squad GreenBoat")),
        ("  Cloud Compliance — 19 regressions", jira_squad_reg_url("Squad Cloud Compliance")),
        ("  Driver — 11 regressions", jira_squad_reg_url("Squad Driver")),
        ("  VRA — 10 regressions", jira_squad_reg_url("Squad VRA")),
        ("  Azure — 8 regressions", jira_squad_reg_url("Squad Cloud Azure")),
        ("  Apex Legends — 8 regressions", jira_squad_reg_url("Squad Apex Legends")),
        ("  Mavka — 5 regressions", jira_squad_reg_url("Squad Mavka")),
        ("  AI Agents — 4 regressions", jira_squad_reg_url("Squad AI Agents")),
        ("  Opus — 4 regressions", jira_squad_reg_url("Squad Cloud Opus")),
        ("  Cyber Resilience — 1 regression", jira_squad_reg_url("Squad Cyber Resilience")),
    ]

    for i, item in enumerate(links):
        if len(item) == 3:
            text, url, is_header = item
        else:
            text, url = item
            is_header = False

        if i == 0:
            para = tf2.paragraphs[0]
        else:
            para = tf2.add_paragraph()

        if not text:
            para.space_after = Pt(4)
            continue

        run = para.add_run()
        run.text = text
        if is_header:
            run.font.size = Pt(16)
            run.font.bold = True
            run.font.color.rgb = ACCENT_BLUE
        else:
            run.font.size = Pt(13)
            run.font.color.rgb = LIGHT_GRAY
            if url:
                run.hyperlink.address = url
                run.font.color.rgb = RGBColor(0x58, 0xA6, 0xFF)  # clickable blue
        para.space_after = Pt(3)

    return slide

add_links_slide()

# 26: Summary
add_content_slide("Summary & Next Steps", [
    ("What went right:", 22, ACCENT_GREEN, True),
    ("  FF improved (-32%), Dana CF 6→2, Rajeev FF 30→11", 16, WHITE, False),
    ("", 8, WHITE, False),
    ("What went wrong:", 22, ACCENT_RED, True),
    ("  Regressions +204% (50→152), CF +57%, Automation rate dropped", 16, WHITE, False),
    ("  6/8 improvements from 10.8 NOT addressed", 16, WHITE, False),
    ("", 8, WHITE, False),
    ("Root causes:", 22, ACCENT_ORANGE, True),
    ("  React/Nils (60), Cloud Compliance (19), QA queue (Rajeev), late requirements", 16, WHITE, False),
    ("", 8, WHITE, False),
    ("For 10.10 — non-negotiables:", 22, ACCENT_BLUE, True),
    ("  1. No tweak activation after Sprint 5", 16, WHITE, False),
    ("  2. RFT WIP limits enforced", 16, WHITE, False),
    ("  3. Mid-release checkpoint at Sprint 4", 16, WHITE, False),
    ("  4. QA capacity aligned to dev output (esp. Rajeev squads)", 16, WHITE, False),
])

# Save
out_path = "retro_109_presentation.pptx"
prs.save(out_path)
print(f"✅ Generated: {out_path} ({len(prs.slides)} slides)")
