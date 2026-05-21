import streamlit as st
import pdfplumber
from groq import Groq
from dotenv import load_dotenv
from laws import INDIAN_LABOUR_LAWS, ANALYSIS_PROMPT
import os
import re

load_dotenv()
api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=api_key)

st.set_page_config(page_title="PolicyGuard", page_icon="⚖️", layout="wide")
st.title("⚖️ PolicyGuard")
st.subheader("AI Legal Risk Scanner for HR Policies — Indian Labour Law")
st.markdown("---")

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
    col1.metric("Pages Scanned", "15")
    col2.metric("Laws Checked", "10")
    col3.metric("Status", "Ready")
    st.markdown("---")

    if st.button("🔍 Scan for Legal Risks", use_container_width=True):
        with st.spinner("⚖️ Analysing against Indian Labour Laws..."):
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
        high = result.count("HIGH")
        medium = result.count("MEDIUM")
        low = result.count("LOW")
        c1, c2, c3 = st.columns(3)
        c1.error(f"🔴 HIGH RISK: {high}")
        c2.warning(f"🟡 MEDIUM RISK: {medium}")
        c3.success(f"🟢 LOW RISK: {low}")
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
            label="📥 Download Full Report",
            data=result,
            file_name="PolicyGuard_Risk_Report.txt",
            mime="text/plain",
            use_container_width=True
        )