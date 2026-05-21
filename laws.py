INDIAN_LABOUR_LAWS = """
You are an expert in Indian Labour Law. Analyse the HR policy against these specific Indian laws:

1. POSH Act 2013 (Sexual Harassment of Women at Workplace)
   - Must have Internal Complaints Committee (ICC)
   - Must have written anti-harassment policy
   - Must conduct annual awareness programs

2. Maternity Benefit Act 1961 (amended 2017)
   - 26 weeks paid maternity leave for first 2 children
   - Creche facility mandatory if 50+ employees
   - Work from home option must be offered

3. Payment of Wages Act 1936
   - Wages must be paid by 7th of every month (establishments with 1000+ employees: 10th)
   - No unauthorised deductions allowed

4. Minimum Wages Act 1948
   - Policy must not specify wages below state minimum wage
   - Must revise wages when government revises minimum wage

5. Payment of Gratuity Act 1972
   - Gratuity mandatory after 5 years of continuous service
   - Formula: 15 days salary x years of service / 26

6. Employees Provident Fund Act 1952
   - Mandatory for establishments with 20+ employees
   - 12% employee contribution + 12% employer contribution

7. Industrial Disputes Act 1947 (Section 9A)
   - 21 days notice required before changing service conditions
   - Cannot change working hours, wages, leave without notice

8. Payment of Bonus Act 1965
   - Minimum 8.33% bonus mandatory
   - Maximum 20% bonus
   - Applicable to employees earning up to Rs 21,000/month

9. Factories Act 1948
   - Max 48 hours work per week
   - Overtime must be paid at double rate
   - Mandatory rest intervals

10. Code on Wages 2019
    - Equal pay for equal work regardless of gender
    - Timely payment obligations
"""

ANALYSIS_PROMPT = """
{laws}

Now analyse this HR Policy:

{policy_text}

Give me a structured analysis in this EXACT format for each issue found:

ISSUE 1:
- Clause: [quote the problematic part]
- Law Violated: [specific law and section]
- Severity: HIGH / MEDIUM / LOW
- Why it's a risk: [1-2 lines explanation]
- Suggested Fix: [specific improvement]

ISSUE 2:
[same format]

And so on. Find at least 5 issues. Be specific to Indian law only.
"""