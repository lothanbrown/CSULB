import streamlit as st
import pandas as pd
from libayshuns_sql_analysis import show_libayshuns_sql_analysis
from libayshuns_payroll_summary import show_libayshuns_payroll_summary
from libayshuns_income_statement import show_libayshuns_income_statement
from libayshuns_questions import show_libayshuns_questions

def show_libayshuns_project():
    st.title("Libayshuns Project – ACCT 605")

    st.markdown("""
    **Libayshuns, Inc.** owns a chain of liquor stores in Oregon and Washington.  
    Analyze their performance for the fiscal year Q4 2023 – Q3 2024.
    """)

    tools = [
        "SQL Queries",
        "Python Analysis",
        "Alteryx Workflows",
        "Excel Analysis",
        "Tableau Visualizations",
        "Project Questions & Answers"
    ]
    st.sidebar.header("Select Analysis Tool")
    tool_choice = st.sidebar.selectbox("Choose a tool:", tools) 
    if tool_choice == "SQL Queries":
        st.subheader("SQL Queries")
        st.markdown("""
        Use SQL to analyze the data. Key queries include:
        1. Revenue by store and quarter.
        2. Cost of goods sold and gross profit margin.
        3. Payroll expenses by store.
        4. Inventory discrepancies.
        5. Best-selling items.
        """)
        st.code("""
        -- Example SQL Query
        SELECT Store, SUM(SalesDollars) AS TotalRevenue
        FROM sales
        GROUP BY Store;
        """, language="sql")
        show_libayshuns_sql_analysis()
    elif tool_choice == "Python Analysis":
        st.subheader("Python Analysis")
        st.markdown("""
        Use Python with Pandas for data manipulation and analysis. Key tasks include:
        1. Data cleaning and preparation.
        2. Calculating revenue, cost of goods sold, and payroll expenses.
        3. Analyzing inventory discrepancies.
        """)
        st.code("""
        import pandas as pd
        sales = pd.read_csv('sales.csv')
        revenue_by_store = sales.groupby('Store')['SalesDollars'].sum()
        """, language="python")
        show_libayshuns_payroll_summary()
    elif tool_choice == "Alteryx Workflows":
        st.subheader("Alteryx Workflows")
        st.markdown("""
        Use Alteryx for data blending and advanced analytics. Key tasks include:
        1. Joining sales data with inventory data.
        2. Calculating cost of goods sold.
        3. Creating visualizations for management reports.
        """)
        st.image("https://example.com/alteryx_workflow_example.png", caption="Alteryx Workflow Example")
    elif tool_choice == "Excel Analysis":
        st.subheader("Excel Analysis")
        st.markdown("""
        Use Excel for quick analysis and visualization. Key tasks include:
        1. Creating pivot tables for revenue analysis.
        2. Using formulas to calculate cost of goods sold.
        3. Visualizing data with charts.
        """)
        st.code("""
        =SUMIF(Sales!A:A, "Store1", Sales!B:B)
        """, language="excel")
        show_libayshuns_income_statement()
    elif tool_choice == "Tableau Visualizations":
        st.subheader("Tableau Visualizations")
        st.markdown("""
        Use Tableau for interactive dashboards. Key visualizations include:
        1. Revenue by store and quarter.
        2. Cost of goods sold by item.
        3. Payroll expenses by store.
        """)
        st.image("https://example.com/tableau_dashboard_example.png", caption="Tableau Dashboard Example")     
    elif tool_choice == "Project Questions & Answers":
        st.subheader("Project Questions & Answers")
        st.markdown("""
        Answer key project questions:
        1. What was the revenue for each store and total revenue for each quarter and for the entire fiscal year?
        2. What was the cost of goods and gross profit margin for each store and in total for each quarter and for the entire fiscal year?
        3. What were the payroll expenses by store and in total for each quarter and for the entire fiscal year?
        4. What was the difference between calculated and actual ending inventory? What contributed to the difference, if any?
        5. Which items in the master inventory list were best sellers?
        6. Was there a difference in the inventory best sellers among stores?
        """)
        show_libayshuns_questions()

