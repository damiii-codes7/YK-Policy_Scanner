import streamlit as st
import pdfplumber
from groq import Groq
from laws import INDIAN_LABOUR_LAWS, ANALYSIS_PROMPT
import os
import re

# API Key
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="PolicyGuard", page_icon="⚖️", layout="wide")

# Dark/Light mode toggle
mode = st.toggle("🌙 Dark Mode", value=True)

if mode:
    bg = "#0e1117"
    text = "#ffffff"
    card = "#1e2130"
else:
    bg = "#ffffff"
    text = "#000000"
    card = "#f0f2f6"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg}; color: {text}; }}
    .block-container {{ padding-top: 2rem; }}
    </style>
""", unsafe_allow_html=True)

# Centered header
st.markdown(f"""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='font-size: 3rem; color: {text};'>⚖️ PolicyGuard</h1>
        <p style='font-size: 1.3rem; color: {"#aaaaaa" if mode else "#555555"};'>
            AI Legal Risk Scanner for HR Policies — Indian Labour Law
        </p>
        <p style='color: {"#888888" if mode else "#777777"}; font-size: 0.9rem;'>
            Upload your HR policy and get an instant compliance report against 10 Indian Labour Laws
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
# How it works section
with st.expander("ℹ️ How does PolicyGuard work?"):
    col1, col2, col3 = st.columns(3)
    col1.info("**Step 1 📄**\nUpload your company's HR or internal policy PDF")
    col2.info("**Step 2 🤖**\nOur AI scans it against 10 Indian Labour Laws")
    col3.info("**Step 3 📋**\nGet a detailed risk report with severity scores and fixes")

st.markdown("---")

# Laws covered
st.markdown("**📚 Laws we check against:**")
laws_cols = st.columns(5)
laws = ["POSH Act 2013", "Maternity Benefit Act", "Min. Wages Act", 
        "Payment of Wages Act", "Gratuity Act", 
        "EPF Act 1952", "Industrial Disputes Act", 
        "Payment of Bonus Act", "Factories Act", "Code on Wages 2019"]
for i, law in enumerate(laws):
    laws_cols[i % 5].success(f"✅ {law}")

st.markdown("---")

# Upload
uploaded_file = st.file_uploader("📂 Upload your HR Policy PDF", type=["pdf"])

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        full_text = ""
        for page in pdf.pages[:15]:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    st.success("✅ Policy uploaded and read successfully!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Pages Scanned", min(15, len(pdf.pages) if hasattr(pdf, 'pages') else 15))
    col2.metric("Laws Checked", "10")
    col3.metric("Status", "Ready to Scan")
    st.markdown("---")

    if st.button("🔍 Scan for Legal Risks", use_container_width=True):
        with st.spinner("⚖️ Analysing against Indian Labour Laws... this may take 30 seconds"):

            prompt = ANALYSIS_PROMPT.format(
                laws=INDIAN_LABOUR_LAWS,
                policy_text=full_text[:4000]
            )

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.choices[0].message.content

        st.markdown("---")
        st.subheader("📋 Legal Risk Report")
        st.caption(f"Analysed: {uploaded_file.name}")

        high = result.count("HIGH")
        medium = result.count("MEDIUM")
        low = result.count("LOW")

        c1, c2, c3 = st.columns(3)
        c1.error(f"🔴 HIGH RISK: {high}")
        c2.warning(f"🟡 MEDIUM RISK: {medium}")
        c3.success(f"🟢 LOW RISK: {low}")

        if high > 0:
            st.error("⚠️ Immediate attention required — HIGH risk issues found!")
        elif medium > 0:
            st.warning("📝 Some issues need review before your next audit.")
        else:
            st.success("🎉 No major issues found!")

        st.markdown("---")

        issues = re.split(r'ISSUE \d+:', result)
        issues = [i.strip() for i in issues if i.strip()]

        for idx, issue in enumerate(issues, 1):
            if "HIGH" in issue:
                color = "🔴"
                expanded = True
            elif "MEDIUM" in issue:
                color = "🟡"
                expanded = False
            else:
                color = "🟢"
                expanded = False

            with st.expander(f"{color} Issue {idx}", expanded=expanded):
                st.markdown(issue)

        st.markdown("---")

        st.download_button(
            label="📥 Download Full Risk Report",
            data=f"PolicyGuard Legal Risk Report\nFile: {uploaded_file.name}\n\n{result}",
            file_name="PolicyGuard_Risk_Report.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.caption("⚖️ PolicyGuard is an AI tool. Always consult a qualified legal professional for final advice.")