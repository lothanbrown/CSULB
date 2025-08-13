import streamlit as st

st.set_page_config(page_title='ACCT 605 Data Analytics Study Guide', layout='wide')

st.title("ACCT 605-01: Data Analytics in Accounting")
st.markdown("""
Welcome to your interactive study guide! Use the sidebar to navigate between topics.
---
""")

topics = [
    "Data Analytic Thinking & IMPACT Framework",
    "Audit, Tax Analytics & Machine Learning",
    "Storytelling & Presentation Skills",
    "Analytics & Visualization Tools",
    "CPA Exam Readiness",
    "Core Concepts & Practice"
]
choice = st.sidebar.radio("Choose a topic:", topics)

if choice == topics[0]:
    st.header("Data Analytic Thinking & IMPACT Framework")
    st.markdown("""
#### **IMPACT Framework**

1. **Identify**: What is the business/accounting question?  
2. **Master**: Prepare, clean, and understand relevant data.  
3. **Perform**: Run analysis, modeling, or testing.  
4. **Address**: Refine or revise based on findings.
5. **Communicate**: Present actionable insights.
6. **Track**: Monitor for changes or improvements.

**Example**:  
Margins are falling.  
- `Identify`: Why?  
- `Master`: Gather 3 years of sales & expenses.  
- `Perform`: Trend analysis.  
- `Address`: Pricing error found, re-run analysis.  
- `Communicate`: Present the error and fix.  
- `Track`: Watch for improvements in margin.

**Practice:**  
Describe your IMPACT steps for investigating rising software expenses.
""")

elif choice == topics[1]:
    st.header("Audit, Tax Analytics & Machine Learning")
    st.subheader("Audit & Tax Analytics")
    st.markdown("""
- **Audit**: Use Benford's Law to check for fraud in vendor invoices.  
- **Tax**: Aggregate sales by state for correct tax reporting.

**Practice:**  
What would you do if you find invoice digit anomalies with Benford’s Law?
""")
    st.subheader("Machine Learning in Accounting")
    st.markdown("""
**Supervised Learning:**  
Predict overdue accounts using payment history.

**Unsupervised Learning:**  
Cluster customer payment patterns.

**Practice:**  
Describe an accounting application for unsupervised learning.
""")

elif choice == topics[2]:
    st.header("Storytelling & Presentation Skills")
    st.markdown("""
**Example:**
"Employee turnover is high" ➔ "Analyzing compensation and exit interviews to suggest retention ideas."

**Decision Model Example:**  
Compare lease vs. buy using sensitivity analysis (Excel).

**Practice:**
- Reframe: "Inventory losses are increasing."
- Outline a 3-slide presentation on rising expenses.
""")

elif choice == topics[3]:
    st.header("Analytics & Visualization Tools")

    st.subheader("Excel")
    st.markdown("""
**Advanced Functions**: `=SUMIFS`, `=VLOOKUP`, Pivot Tables

**Practice:**  
Highlight all sales over $50,000 where customer name is blank.
""")
    st.subheader("Tableau")
    st.markdown("""
Create line & bar charts, dashboard with filters.

**Practice:**  
Dashboard to compare 3 product lines across regions.
""")
    st.subheader("SQL")
    st.markdown("""
**Example:**  
```sql
SELECT Vendor, SUM(Amount) FROM Payments WHERE Year=2023 GROUP BY Vendor HAVING SUM(Amount) > 10000;
```
""")