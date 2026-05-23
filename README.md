# ⚖️ PolicyGuard — Legal Intelligence Platform

> **AI-powered legal tools for Indian law. Built for MSMEs, HR teams, lawyers, and anyone who needs legal clarity fast.**

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57-red)
![Groq](https://img.shields.io/badge/Groq-Llama%203.1-orange)
![License](https://img.shields.io/badge/License-Open%20Source-green)

---

## 🌐 Live App

👉 **[policyguard-riskmanagementanalysis.streamlit.app](https://policyguard-riskmanagementanalysis.streamlit.app)**

---

## 🛠️ What is PolicyGuard?

PolicyGuard is a two-in-one AI legal intelligence platform built specifically for Indian law. Upload any legal document and get an instant, structured analysis — powered by Llama 3.1 via Groq API.

---

## ⚡ Features

### Tab 1 — ⚖️ Policy Scanner
Upload your company's HR or internal policy PDF and get an instant compliance report checked against **10 major Indian Labour Laws.**

**What it checks:**
| Law | Key Provisions |
|---|---|
| POSH Act 2013 | ICC formation, anti-harassment policy, awareness programs |
| Maternity Benefit Act 1961 (amended 2017) | 26 weeks leave, creche facility, WFH option |
| Payment of Wages Act 1936 | Payment timelines, unauthorised deductions |
| Minimum Wages Act 1948 | Wages vs state minimum wage |
| Payment of Gratuity Act 1972 | 5-year threshold, formula |
| EPF Act 1952 | 12%+12% contribution, 20+ employees |
| Industrial Disputes Act 1947 | 21-day notice for service condition changes |
| Payment of Bonus Act 1965 | 8.33% minimum, 20% maximum |
| Factories Act 1948 | 48hr week, double overtime rate |
| Code on Wages 2019 | Equal pay, timely payment |

**Output:**
- 🔴 HIGH RISK issues (open by default)
- 🟡 MEDIUM RISK issues
- 🟢 LOW RISK issues
- Downloadable risk report (.txt)

---

### Tab 2 — 📜 Judgment Summarizer
Upload any Indian court judgment PDF and get an instant AI-powered summary.

**Summary types:**
- Full Summary — Facts, issues, decision, ratio decidendi
- Quick Summary — 5 bullet points only
- Legal Issues Only — What questions did the court answer?
- Final Order Only — What did the court decide?
- Landmark Analysis — Why is this judgment important?

**Output includes:**
- Case name & citation
- Court & date
- Key facts
- Legal issues addressed
- Decision & ratio decidendi
- Significance of the judgment
- Downloadable summary (.txt)

---

## 🏗️ Tech Stack

| Component | Technology |
|---|---|
| AI Model | Llama 3.1 8B (Meta — open source) |
| AI API | Groq API (free tier) |
| Web Framework | Streamlit |
| PDF Processing | pdfplumber |
| Deployment | Streamlit Community Cloud |
| Version Control | GitHub |

---
---

## 🎯 Who is this for?

- **MSME Owners** — Check if your HR policy is legally compliant
- **HR Managers** — Identify risks before audits
- **Startups** — Ensure compliance from day one
- **Law Students** — Quickly summarise court judgments
- **Lawyers** — First-pass analysis before detailed review
- **Compliance Officers** — Regular policy health checks

---

## 📜 Indian Laws Covered

PolicyGuard checks against Indian law specifically — not generic global compliance advice.

Laws covered include the POSH Act 2013, Maternity Benefit Act 1961 (2017 amendment), Payment of Wages Act 1936, Minimum Wages Act 1948, Payment of Gratuity Act 1972, EPF Act 1952, Industrial Disputes Act 1947, Payment of Bonus Act 1965, Factories Act 1948, and Code on Wages 2019.

---

## ⚠️ Disclaimer

PolicyGuard is an AI-powered tool designed to assist with legal awareness. It is **not a substitute for qualified legal advice.** Always consult a qualified legal professional before making compliance decisions.

---

## 🏆 Built For

**The Code of Law Challenge** — Rhett Legal-Tech Hackathon
Track: AI for Legal Governance (Open Innovation)
Built solo in 8 days.

---

## 👩‍💻 Built By

**Damini** — Law background meets legal-tech.



```bash
