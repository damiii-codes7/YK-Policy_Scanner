from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ---- DOCUMENT SETUP ----
doc = SimpleDocTemplate(
    "PolicyGuard_Submission.pdf",
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# ---- COLORS ----
BLACK = colors.HexColor('#030303')
ORANGE = colors.HexColor('#E94E1B')
WHITE = colors.white
GREY = colors.HexColor('#888888')
LIGHTGREY = colors.HexColor('#181818')

# ---- STYLES ----
styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title',
    fontName='Helvetica-Bold',
    fontSize=36,
    textColor=WHITE,
    spaceAfter=10,
    alignment=TA_CENTER,
    leading=40
)

subtitle_style = ParagraphStyle('Subtitle',
    fontName='Helvetica',
    fontSize=14,
    textColor=GREY,
    spaceAfter=30,
    alignment=TA_CENTER
)

section_style = ParagraphStyle('Section',
    fontName='Helvetica-Bold',
    fontSize=18,
    textColor=ORANGE,
    spaceBefore=20,
    spaceAfter=10,
    leading=22
)

body_style = ParagraphStyle('Body',
    fontName='Helvetica',
    fontSize=10,
    textColor=WHITE,
    spaceAfter=8,
    leading=16,
    alignment=TA_JUSTIFY
)

bold_body_style = ParagraphStyle('BoldBody',
    fontName='Helvetica-Bold',
    fontSize=10,
    textColor=WHITE,
    spaceAfter=8,
    leading=16
)

small_style = ParagraphStyle('Small',
    fontName='Helvetica',
    fontSize=9,
    textColor=GREY,
    spaceAfter=6,
    leading=14
)

label_style = ParagraphStyle('Label',
    fontName='Helvetica-Bold',
    fontSize=8,
    textColor=ORANGE,
    spaceAfter=4,
    leading=12
)

# ---- CONTENT ----
story = []

def divider():
    story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=15, spaceBefore=15))

def section(title):
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(title, section_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=GREY, spaceAfter=10))

def body(text):
    story.append(Paragraph(text, body_style))

def bold(text):
    story.append(Paragraph(text, bold_body_style))

def space():
    story.append(Spacer(1, 0.5*cm))

# ===========================
# COVER PAGE
# ===========================

# Dark background table for cover
cover_data = [[
    Paragraph("⚖", ParagraphStyle('Icon', fontName='Helvetica-Bold', fontSize=48, textColor=ORANGE, alignment=TA_CENTER)),
]]
cover_table = Table(cover_data, colWidths=[17*cm])
cover_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), BLACK),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 40),
    ('BOTTOMPADDING', (0,0), (-1,-1), 20),
]))
story.append(cover_table)

story.append(Paragraph("POLICYGUARD", ParagraphStyle('BigTitle',
    fontName='Helvetica-Bold', fontSize=48, textColor=WHITE,
    alignment=TA_CENTER, spaceAfter=5)))

story.append(Paragraph("AI Legal Risk Scanner for HR Policies", ParagraphStyle('CoverSub',
    fontName='Helvetica', fontSize=16, textColor=GREY,
    alignment=TA_CENTER, spaceAfter=5)))

story.append(Paragraph("Indian Labour Law Compliance", ParagraphStyle('CoverSub2',
    fontName='Helvetica-Bold', fontSize=14, textColor=ORANGE,
    alignment=TA_CENTER, spaceAfter=30)))

divider()

# Info table
info_data = [
    [Paragraph("HACKATHON", label_style), Paragraph("The Code of Law Challenge — Rhett Legal", body_style)],
    [Paragraph("TRACK", label_style), Paragraph("AI for Legal Governance (Open Innovation)", body_style)],
    [Paragraph("PARTICIPANT", label_style), Paragraph("Damini", body_style)],
    [Paragraph("SUBMISSION DATE", label_style), Paragraph("May 30-31, 2026", body_style)],
    [Paragraph("LIVE APP", label_style), Paragraph("policyguard-riskmanagementanalysis.streamlit.app", body_style)],
    [Paragraph("GITHUB", label_style), Paragraph("github.com/damiii-codes7/PolicyGuard", body_style)],
]
info_table = Table(info_data, colWidths=[4*cm, 13*cm])
info_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), BLACK),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.HexColor('#0a0a0a'), BLACK]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(info_table)
space()

from reportlab.platypus import PageBreak
story.append(PageBreak())

# ===========================
# SECTION 1: PROBLEM STATEMENT
# ===========================
section("01 / PROBLEM STATEMENT")

body("India has over 63 million Micro, Small, and Medium Enterprises (MSMEs) employing hundreds of millions of workers across diverse industries. Yet the vast majority of these businesses operate without dedicated legal teams or compliance officers.")

space()

body("Indian labour law is extensive and fragmented — spanning 10+ central acts, numerous state-level variations, and 4 newly consolidated Labour Codes enacted between 2019 and 2020. This complexity makes genuine compliance extremely difficult for growing businesses, particularly those in tier 2 and tier 3 cities where access to quality legal support is limited.")

space()

bold("The consequences of non-compliance are serious:")

issues_data = [
    ["01", "Financial penalties and government fines"],
    ["02", "Employee disputes and wrongful termination claims"],
    ["03", "Regulatory inspections and enforcement action"],
    ["04", "Reputational damage affecting hiring and partnerships"],
    ["05", "Personal liability for directors and HR managers"],
]
issues_table = Table(issues_data, colWidths=[1.5*cm, 15.5*cm])
issues_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,0), (0,-1), ORANGE),
    ('TEXTCOLOR', (1,0), (1,-1), WHITE),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(issues_table)
space()

body("Current solutions are inadequate: law firms are expensive, generic compliance checklists are imprecise, and enterprise software is inaccessible to small businesses. There is no simple, affordable, AI-powered tool that a non-lawyer business owner can use to instantly check if their HR policies are legally compliant.")

space()
bold("PolicyGuard solves this gap.")
story.append(PageBreak())

# ===========================
# SECTION 2: SOLUTION OVERVIEW
# ===========================
section("02 / SOLUTION OVERVIEW")

body("PolicyGuard is an AI-powered web application that allows any business to upload their HR or internal policy document and receive an instant, structured legal risk report — checked against 10 major Indian Labour Laws.")

space()

bold("Core Value Proposition:")
body("Upload your policy. Get your risks. Fix them before they cost you.")

space()

sol_data = [
    [Paragraph("SIMPLE", label_style), Paragraph("Upload a PDF → Get a report. No login, no complex setup, no legal jargon.", body_style)],
    [Paragraph("SPECIFIC", label_style), Paragraph("Checks against specific sections of actual Indian laws — not generic advice.", body_style)],
    [Paragraph("ACTIONABLE", label_style), Paragraph("Every flagged issue comes with a suggested fix — not just a warning.", body_style)],
    [Paragraph("ACCESSIBLE", label_style), Paragraph("Free to use. Works on any device. No legal background required.", body_style)],
    [Paragraph("FAST", label_style), Paragraph("Full analysis in under 60 seconds. No waiting for a lawyer's appointment.", body_style)],
]
sol_table = Table(sol_data, colWidths=[3*cm, 14*cm])
sol_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0a0a0a')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(sol_table)
space()

body("PolicyGuard is not a replacement for legal counsel — it is a first line of defence that makes compliance awareness accessible to every business, regardless of size or budget.")
story.append(PageBreak())

# ===========================
# SECTION 3: HOW IT WORKS
# ===========================
section("03 / HOW IT WORKS")

bold("User Journey:")
steps_data = [
    ["STEP 01", "User uploads HR/internal policy PDF through the web interface"],
    ["STEP 02", "pdfplumber extracts text from up to 15 pages of the document"],
    ["STEP 03", "Extracted text is combined with Indian Labour Law knowledge base"],
    ["STEP 04", "Combined prompt is sent to Llama 3.1 model via Groq API"],
    ["STEP 05", "AI analyses content and returns structured risk findings"],
    ["STEP 06", "App parses and displays colour-coded issues with severity scores"],
    ["STEP 07", "User downloads full risk report as a text file"],
]
steps_table = Table(steps_data, colWidths=[2.5*cm, 14.5*cm])
steps_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,0), (0,-1), ORANGE),
    ('TEXTCOLOR', (1,0), (1,-1), WHITE),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(steps_table)
space()

bold("Risk Severity Scoring:")
sev_data = [
    ["🔴 HIGH", "Direct violation of a mandatory legal provision. Immediate action required. Could result in penalties or legal action."],
    ["🟡 MEDIUM", "Ambiguous or potentially non-compliant clause. Should be reviewed and clarified by legal counsel."],
    ["🟢 LOW", "Minor gap or best-practice deviation. Low immediate risk but worth addressing."],
]
sev_table = Table(sev_data, colWidths=[2.5*cm, 14.5*cm])
sev_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,0), (-1,-1), WHITE),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(sev_table)
story.append(PageBreak())

# ===========================
# SECTION 4: LAWS COVERED
# ===========================
section("04 / INDIAN LABOUR LAWS COVERED")

body("PolicyGuard checks uploaded policies against the following 10 central Indian Labour Laws:")
space()

laws_data = [
    ["LAW", "KEY PROVISIONS CHECKED"],
    ["POSH Act 2013", "ICC formation, written anti-harassment policy, annual awareness programs"],
    ["Maternity Benefit Act 1961\n(amended 2017)", "26 weeks paid leave for first 2 children, creche facility (50+ employees), WFH option"],
    ["Payment of Wages Act 1936", "Payment by 7th/10th of month, no unauthorised deductions"],
    ["Minimum Wages Act 1948", "Wages not below state minimum, revision when government revises"],
    ["Payment of Gratuity Act 1972", "Mandatory after 5 years, formula: 15 days x years / 26"],
    ["EPF Act 1952", "Mandatory for 20+ employees, 12%+12% contribution structure"],
    ["Industrial Disputes Act 1947\n(Section 9A)", "21 days notice before changing service conditions"],
    ["Payment of Bonus Act 1965", "Minimum 8.33%, maximum 20%, applicable up to Rs 21,000/month"],
    ["Factories Act 1948", "Max 48 hours/week, double rate for overtime, mandatory rest intervals"],
    ["Code on Wages 2019", "Equal pay for equal work regardless of gender, timely payment"],
]
laws_table = Table(laws_data, colWidths=[5*cm, 12*cm])
laws_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), ORANGE),
    ('TEXTCOLOR', (0,0), (-1,0), BLACK),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,1), (-1,-1), WHITE),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#0a0a0a'), colors.HexColor('#060606')]),
]))
story.append(laws_table)
story.append(PageBreak())

# ===========================
# SECTION 5: TECH STACK
# ===========================
section("05 / TECHNOLOGY STACK")

body("PolicyGuard is built entirely on open-source technologies, in compliance with the hackathon's open innovation track requirements.")
space()

tech_data = [
    ["COMPONENT", "TECHNOLOGY", "LICENCE", "PURPOSE"],
    ["AI Model", "Llama 3.1 8B\n(Meta)", "Llama 3 Community", "Legal analysis and risk identification"],
    ["AI API", "Groq API", "Open (free tier)", "Fast inference for open-source LLMs"],
    ["Web Framework", "Streamlit", "Apache 2.0", "UI and application logic"],
    ["PDF Processing", "pdfplumber", "MIT", "Text extraction from uploaded PDFs"],
    ["Secret Management", "python-dotenv", "BSD", "Secure API key handling"],
    ["Deployment", "Streamlit Cloud", "Free tier", "Live hosting from GitHub"],
    ["Version Control", "GitHub", "Free", "Code management and CI/CD"],
]
tech_table = Table(tech_data, colWidths=[3.5*cm, 4*cm, 3.5*cm, 6*cm])
tech_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), ORANGE),
    ('TEXTCOLOR', (0,0), (-1,0), BLACK),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,1), (-1,-1), WHITE),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#0a0a0a'), colors.HexColor('#060606')]),
]))
story.append(tech_table)
story.append(PageBreak())

# ===========================
# SECTION 6: IMPACT & USE CASES
# ===========================
section("06 / REAL-WORLD IMPACT")

body("PolicyGuard directly addresses the compliance gap faced by India's 63 million MSMEs — particularly in tier 2 and tier 3 cities where legal support is scarce and expensive.")

space()
bold("Primary Target Users:")

users_data = [
    ["HR Managers", "Review and update internal policies before audits"],
    ["MSME Owners", "Understand compliance obligations without hiring a lawyer"],
    ["Startups", "Ensure HR policies are compliant from day one"],
    ["Law Firms", "Quick preliminary scan before detailed manual review"],
    ["Compliance Officers", "Regular policy health checks across departments"],
]
users_table = Table(users_data, colWidths=[4*cm, 13*cm])
users_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,0), (0,-1), ORANGE),
    ('TEXTCOLOR', (1,0), (1,-1), WHITE),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(users_table)
space()

bold("Example Scenario:")
body("A 50-person manufacturing startup in Coimbatore has an HR policy manual written 3 years ago. They upload it to PolicyGuard. Within 60 seconds, they discover:")
body("• Their maternity leave clause still says 12 weeks — violating the 2017 amendment that mandates 26 weeks (HIGH RISK)")
body("• No Internal Complaints Committee is mentioned anywhere — direct POSH Act violation (HIGH RISK)")
body("• Overtime pay is described as 1.5x the regular rate — Factories Act requires 2x (MEDIUM RISK)")
body("They fix all three issues before their next HR audit — avoiding potential penalties and employee grievances.")
story.append(PageBreak())

# ===========================
# SECTION 7: EVALUATION CRITERIA MATCH
# ===========================
section("07 / EVALUATION CRITERIA ALIGNMENT")

eval_data = [
    ["CRITERION", "HOW POLICYGUARD ADDRESSES IT"],
    ["Innovation &\nProblem Relevance", "First AI tool specifically targeting Indian HR policy compliance. Addresses a real, underserved gap in the MSME legal ecosystem — directly aligned with Rhett's mission."],
    ["Practical Utility in\nReal-World Legal Scenarios", "Live, deployed application accessible at a public URL. Can be used by any business right now. Tested against real HR policy documents."],
    ["Effective Use of\nOpen-Source Technologies", "Built on Llama 3.1 (Meta's open-source LLM) via Groq, Streamlit (Apache 2.0), pdfplumber (MIT). Fully open-source stack."],
    ["Simplicity &\nScalability", "Single-page interface: upload → scan → report. Architecture can scale to support more laws, languages, and document types with minimal changes."],
]
eval_table = Table(eval_data, colWidths=[4*cm, 13*cm])
eval_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), ORANGE),
    ('TEXTCOLOR', (0,0), (-1,0), BLACK),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,1), (-1,-1), WHITE),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (1,1), (1,-1), 'Helvetica'),
    ('TEXTCOLOR', (0,1), (0,-1), ORANGE),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#0a0a0a'), colors.HexColor('#060606')]),
]))
story.append(eval_table)
story.append(PageBreak())

# ===========================
# SECTION 8: FUTURE ROADMAP
# ===========================
section("08 / FUTURE ROADMAP")

body("PolicyGuard is designed as a foundation that can be expanded significantly:")
space()

road_data = [
    ["PHASE 1\n(0-3 months)", "• Support for employment contracts, NDAs, service agreements\n• State-specific law variations (Tamil Nadu, Maharashtra, Karnataka)\n• Multilingual output (Tamil, Hindi)"],
    ["PHASE 2\n(3-6 months)", "• Auto-generate compliant policy templates based on scan results\n• Regulatory change alerts when Indian labour laws are amended\n• PDF report with company branding"],
    ["PHASE 3\n(6-12 months)", "• Integration with HRMS systems (Zoho, Darwinbox)\n• API for law firms and compliance platforms\n• Dashboard for tracking compliance over time"],
    ["PHASE 4\n(12+ months)", "• Expand to other South Asian jurisdictions (Sri Lanka, Bangladesh)\n• Enterprise tier with audit trail and team collaboration\n• Fine-tuned legal LLM trained on Indian case law"],
]
road_table = Table(road_data, colWidths=[3*cm, 14*cm])
road_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0a0a0a')),
    ('TEXTCOLOR', (0,0), (0,-1), ORANGE),
    ('TEXTCOLOR', (1,0), (1,-1), WHITE),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#181818')),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(road_table)
story.append(PageBreak())

# ===========================
# SECTION 9: CONCLUSION
# ===========================
section("09 / CONCLUSION")

body("PolicyGuard demonstrates that AI can make legal compliance genuinely accessible — not just for large corporations with legal teams, but for every business in India, regardless of size or location.")

space()

body("By combining open-source AI (Llama 3.1), a curated Indian labour law knowledge base, and a simple upload-and-scan interface, PolicyGuard delivers real legal intelligence in under 60 seconds.")

space()

body("This project was built solo in 8 days — from zero to a live, deployed, functional legal-tech product. It reflects both technical execution and deep understanding of the Indian legal landscape.")

space()

body("The foundation is solid. The use cases are real. The impact is immediate.")

space()
space()

story.append(Paragraph("POLICYGUARD", ParagraphStyle('FinalTitle',
    fontName='Helvetica-Bold', fontSize=28, textColor=WHITE,
    alignment=TA_CENTER, spaceAfter=5)))

story.append(Paragraph("Legal compliance. Made accessible.", ParagraphStyle('FinalSub',
    fontName='Helvetica', fontSize=14, textColor=ORANGE,
    alignment=TA_CENTER, spaceAfter=20)))

divider()

story.append(Paragraph("policyguard-riskmanagementanalysis.streamlit.app", ParagraphStyle('Link',
    fontName='Helvetica', fontSize=10, textColor=GREY,
    alignment=TA_CENTER, spaceAfter=5)))

story.append(Paragraph("github.com/damiii-codes7/PolicyGuard", ParagraphStyle('Link2',
    fontName='Helvetica', fontSize=10, textColor=GREY,
    alignment=TA_CENTER)))

# ---- BUILD PDF ----
def black_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BLACK)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.restoreState()

doc.build(story, onFirstPage=black_background, onLaterPages=black_background)
print("✅ PDF created: PolicyGuard_Submission.pdf")
