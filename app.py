import streamlit as st
import pdfplumber
from groq import Groq
import os
import re
from laws import INDIAN_LABOUR_LAWS, ANALYSIS_PROMPT

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="YK Policy", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Bebas+Neue&display=swap');
.stApp { background-color: #030303 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; }
.stTabs [data-baseweb="tab-list"] { background-color: #030303 !important; border-bottom: 1px solid #181818 !important; gap: 0 !important; }
.stTabs [data-baseweb="tab"] { background-color: #030303 !important; color: #888 !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; border: 1px solid #181818 !important; border-bottom: none !important; padding: 0.75rem 2rem !important; }
.stTabs [aria-selected="true"] { background-color: #E94E1B !important; color: #030303 !important; font-weight: 700 !important; }
.stButton > button { background: transparent !important; color: #E94E1B !important; border: 1px solid #E94E1B !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; padding: 1rem 2rem !important; transition: all 0.3s ease !important; width: 100% !important; }
.stButton > button:hover { background: #E94E1B !important; color: #030303 !important; }
div[data-testid="metric-container"] { background: transparent !important; border: 1px solid #181818 !important; padding: 1.5rem !important; }
div[data-testid="metric-container"] label { font-family: 'Space Mono', monospace !important; font-size: 0.6rem !important; letter-spacing: 0.2em !important; text-transform: uppercase !important; color: #888 !important; }
div[data-testid="metric-container"] div[data-testid="stMetricValue"] { font-family: 'Bebas Neue', sans-serif !important; font-size: 2.5rem !important; color: #ffffff !important; }
.stExpander { border: 1px solid #181818 !important; background: transparent !important; border-radius: 0 !important; }
.stDownloadButton > button { background: #E94E1B !important; color: #030303 !important; border: 1px solid #E94E1B !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; font-weight: 700 !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; padding: 1rem 2rem !important; }
hr { border-color: #181818 !important; }
.stMarkdown p { color: #888 !important; font-size: 0.8rem !important; }
.stSelectbox > div { background: #030303 !important; border: 1px solid #181818 !important; color: #888 !important; font-family: 'Space Mono', monospace !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes ringPulse { 0%{opacity:0.15;transform:translate(-50%,-50%) scale(0.3)} 100%{opacity:0;transform:translate(-50%,-50%) scale(1)} }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
@keyframes slideUp { to{transform:translateY(0)} }
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
</style>
<div style='text-align:center; padding:6vh 2rem 3vh 2rem; position:relative; overflow:hidden;'>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #E94E1B;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease infinite;pointer-events:none;'></div>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #E94E1B;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease 2s infinite;pointer-events:none;'></div>
<div style='display:inline-flex;align-items:center;gap:0.75rem;font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#888;margin-bottom:2rem;padding:0.6rem 1.2rem;border:1px solid #181818;'>
<span style='width:6px;height:6px;background:#E94E1B;border-radius:50%;animation:pulse 2s infinite;display:inline-block;'></span>
AI-Powered &nbsp;|&nbsp; Indian Legal Intelligence &nbsp;|&nbsp; Powered by Llama 3.1
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.3s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#ffffff;letter-spacing:0.02em;'>YK</div>
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#E94E1B;letter-spacing:0.02em;'>POLICY</div>
</div>
<div style='overflow:hidden;margin-bottom:2rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.7s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(1.5rem,4vw,3rem);line-height:0.9;color:#888;'>AI Legal Intelligence — Indian Law Made Accessible</div>
</div>
</div>
<hr style='border-color:#181818;margin:0;'>
<div style='overflow:hidden;padding:1rem 0;border-bottom:1px solid #181818;'>
<div style='display:flex;width:max-content;animation:marquee 30s linear infinite;font-family:Space Mono,monospace;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#444;white-space:nowrap;'>
<span style='padding:0 2rem;'>POSH Act 2013</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Maternity Benefit Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Minimum Wages Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Payment of Wages Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Gratuity Act 1972</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>EPF Act 1952</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Industrial Disputes Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Factories Act 1948</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Code on Wages 2019</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Court Judgment Summarizer</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>POSH Act 2013</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Maternity Benefit Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Minimum Wages Act</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Code on Wages 2019</span><span style='color:#E94E1B;padding:0 1rem;'>◆</span>
</div>
</div>
""", unsafe_allow_html=True)

# ---- TABS ----
tab1, tab2 = st.tabs(["⚖️  Policy Scanner", "📜  Judgment Summarizer"])

# ============================================================
# TAB 1: POLICY SCANNER
# ============================================================
with tab1:
    st.markdown("""
    <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
    letter-spacing:0.2em;color:#888;margin:3rem 0 1rem 0;'>
    01 / UPLOAD TARGET DOCUMENT
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed", key="policy")

    if uploaded_file:
        with pdfplumber.open(uploaded_file) as pdf:
            full_text = ""
            total_pages = len(pdf.pages)
            for page in pdf.pages[:15]:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

        st.markdown(f"""
        <div style='border:1px solid #E94E1B;padding:1rem 1.5rem;margin:1rem 0;
        font-family:Space Mono,monospace;font-size:0.7rem;color:#E94E1B;letter-spacing:0.05em;'>
        ◆ DOCUMENT LOADED — {uploaded_file.name}
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("PAGES SCANNED", min(15, total_pages))
        col2.metric("LAWS CHECKED", "10")
        col3.metric("STATUS", "READY")

        st.markdown("""
        <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
        letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
        02 / INITIATE SCAN
        </div>
        """, unsafe_allow_html=True)

        if st.button("RUN LEGAL RISK ANALYSIS →", use_container_width=True, key="scan"):
            with st.spinner("Scanning against Indian Labour Laws..."):
                prompt = ANALYSIS_PROMPT.format(
                    laws=INDIAN_LABOUR_LAWS,
                    policy_text=full_text[:4000]
                )
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content

            high = result.count("HIGH")
            medium = result.count("MEDIUM")
            low = result.count("LOW")

            st.markdown("""
            <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
            letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
            03 / RISK REPORT
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='display:grid;grid-template-columns:1fr 1fr 1fr;border:1px solid #181818;margin-bottom:2rem;'>
            <div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
            <div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:0.5rem;'>HIGH RISK</div>
            <div style='font-family:Bebas Neue,sans-serif;font-size:4rem;color:#E94E1B;line-height:1;'>{high}</div>
            </div>
            <div style='padding:2rem;border-right:1px solid #181818;text-align:center;'>
            <div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:0.5rem;'>MEDIUM RISK</div>
            <div style='font-family:Bebas Neue,sans-serif;font-size:4rem;color:#ffffff;line-height:1;'>{medium}</div>
            </div>
            <div style='padding:2rem;text-align:center;'>
            <div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#888;margin-bottom:0.5rem;'>LOW RISK</div>
            <div style='font-family:Bebas Neue,sans-serif;font-size:4rem;color:#444;line-height:1;'>{low}</div>
            </div>
            </div>
            """, unsafe_allow_html=True)

            issues = re.split(r'ISSUE \d+:', result)
            issues = [i.strip() for i in issues if i.strip()]

            for idx, issue in enumerate(issues, 1):
                if "HIGH" in issue:
                    label = "🔴 HIGH RISK"
                    expanded = True
                elif "MEDIUM" in issue:
                    label = "🟡 MEDIUM RISK"
                    expanded = False
                else:
                    label = "🟢 LOW RISK"
                    expanded = False

                with st.expander(f"{label} — VIOLATION {idx:02d}", expanded=expanded):
                    st.markdown(issue)

            st.markdown("<hr style='border-color:#181818;margin:2rem 0;'>", unsafe_allow_html=True)

            st.download_button(
                label="EXPORT RISK REPORT →",
                data=f"POLICYGUARD LEGAL RISK REPORT\nDocument: {uploaded_file.name}\n\n{result}",
                file_name="PolicyGuard_Risk_Report.txt",
                mime="text/plain",
                use_container_width=True,
                key="download_policy"
            )

            st.markdown("""
            <div style='text-align:center;margin-top:1rem;padding-bottom:4vh;'>
            <span style='font-family:Space Mono,monospace;font-size:0.6rem;color:#444;letter-spacing:0.1em;'>
            PolicyGuard is an AI tool. Consult a qualified legal professional for final advice.
            </span>
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# TAB 2: JUDGMENT SUMMARIZER
# ============================================================
with tab2:
    st.markdown("""
    <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
    letter-spacing:0.2em;color:#888;margin:3rem 0 1rem 0;'>
    01 / UPLOAD COURT JUDGMENT
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-family:Bebas Neue,sans-serif;font-size:clamp(2rem,6vw,4rem);
    color:#ffffff;margin-bottom:0.5rem;'>JUDGMENT SUMMARIZER</div>
    <div style='font-family:Space Mono,monospace;font-size:0.8rem;
    color:#888;margin-bottom:2rem;'>
    Upload any court judgment PDF → Get an instant AI-powered summary
    </div>
    """, unsafe_allow_html=True)

    judgment_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed", key="judgment")

    if judgment_file:
        with pdfplumber.open(judgment_file) as pdf:
            judgment_text = ""
            total_pages = len(pdf.pages)
            for page in pdf.pages[:20]:
                text = page.extract_text()
                if text:
                    judgment_text += text + "\n"

        st.markdown(f"""
        <div style='border:1px solid #E94E1B;padding:1rem 1.5rem;margin:1rem 0;
        font-family:Space Mono,monospace;font-size:0.7rem;color:#E94E1B;'>
        ◆ JUDGMENT LOADED — {judgment_file.name} // {total_pages} PAGES
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("PAGES READ", min(20, total_pages))
        col2.metric("WORDS", len(judgment_text.split()))
        col3.metric("STATUS", "READY")

        st.markdown("""
        <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
        letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
        02 / SELECT SUMMARY TYPE
        </div>
        """, unsafe_allow_html=True)

        summary_type = st.selectbox("", [
            "Full Summary — Key facts, issues, decision, ratio",
            "Quick Summary — 5 bullet points only",
            "Legal Issues Only — What questions did the court answer?",
            "Final Order Only — What did the court decide?",
            "Landmark Analysis — Why is this judgment important?"
        ], label_visibility="collapsed")

        if st.button("📜 GENERATE SUMMARY →", use_container_width=True, key="summarize"):
            with st.spinner("Reading judgment and generating summary..."):

                summary_prompt = f"""You are an expert Indian legal analyst.
Read this court judgment carefully and provide a {summary_type}.

Format your response with these clearly labelled sections:
CASE NAME & CITATION: [if visible]
COURT & DATE: [if visible]
FACTS: [2-3 sentences on key facts]
LEGAL ISSUES: [what questions the court addressed]
DECISION: [what the court decided]
RATIO DECIDENDI: [the legal reasoning/principle]
SIGNIFICANCE: [why this judgment matters]

Judgment text:
{judgment_text[:5000]}"""

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": summary_prompt}]
                )
                summary = response.choices[0].message.content

            st.markdown("""
            <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
            letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
            03 / JUDGMENT SUMMARY
            </div>
            """, unsafe_allow_html=True)

            st.markdown(summary)

            st.markdown("<hr style='border-color:#181818;margin:2rem 0;'>", unsafe_allow_html=True)

            st.download_button(
                label="EXPORT SUMMARY →",
                data=f"POLICYGUARD — JUDGMENT SUMMARY\nFile: {judgment_file.name}\nType: {summary_type}\n\n{summary}",
                file_name="Judgment_Summary.txt",
                mime="text/plain",
                use_container_width=True,
                key="download_judgment"
            )

            st.markdown("""
            <div style='text-align:center;margin-top:1rem;padding-bottom:4vh;'>
            <span style='font-family:Space Mono,monospace;font-size:0.6rem;color:#444;letter-spacing:0.1em;'>
            PolicyGuard is an AI tool. Always verify with the original judgment text.
            <div style='text-align:center;padding:1rem;font-family:Space Mono,monospace;
font-size:0.55rem;color:#333;text-transform:uppercase;letter-spacing:0.1em;'>
Adv. Damini Yasodai — YK Legal
</div>

            </span>
            </div>
            """, unsafe_allow_html=True)
