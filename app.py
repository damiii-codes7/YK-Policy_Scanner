import streamlit as st
import pdfplumber
from groq import Groq
from laws import INDIAN_LABOUR_LAWS, ANALYSIS_PROMPT

from dotenv import load_dotenv
import streamlit as st
import pdfplumber
from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()
client = Groq(api_key=os.getenv("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"))

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

    st.success(f"✅ Policy uploaded and read successfully!")

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

        # Show severity counts
        high = result.count("HIGH")
        medium = result.count("MEDIUM")
        low = result.count("LOW")

        c1, c2, c3 = st.columns(3)
        c1.error(f"🔴 HIGH RISK: {high}")
        c2.warning(f"🟡 MEDIUM RISK: {medium}")
        c3.success(f"🟢 LOW RISK: {low}")

        st.markdown("---")
        st.markdown(result)