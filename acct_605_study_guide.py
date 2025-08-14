import streamlit as st
from nfl_team_perf_app import show_nfl_team_perf_app
from nfl_text_functions_app import show_nfl_text_functions_app
from sec_date_functions_app import show_sec_date_functions_app
from financial_pmt_app import show_financial_pmt_app
from data_analysis_app import show_data_analysis_app
from slainte_brewery_db_manager import show_slainte_brewery_db_manager
from eu_superstore_dashboard import show_eu_superstore_dashboard
from libayshuns_project import show_libayshuns_project

st.set_page_config(page_title='ACCT 605 Data Analytics Study Guide', layout='wide')

st.title("ACCT 605-01: Data Analytics in Accounting")
st.markdown("""
Welcome to your interactive practice guide!
Use the sidebar to navigate between topics.
---
""")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000; /* Black background */
    }
    .css-18e3th9 {
        background-color: #222222 !important;
    }
    .css-1d391kg {
        color: #FFC72C !important;
    }
    .stButton>button {
        background-color: #FFC72C;
        color: #000;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
topics = [
    "Excel Review",
    "Statistics",
    "SQL Practice",
    "Alteryx Cloud",
    "Python",
    "Tableau",
    "Libayshuns Project" 
]
choice = st.sidebar.selectbox("Choose a topic:", topics)

if choice == topics[0]:
    st.header("Excel Review")
    excel_func = st.radio(
        "Choose an Excel function to practice:",
        [
            "Text Functions", 
            "Date Functions", 
            "PMT Financial Function"
        ]
    )

    if excel_func == "Text Functions":
        show_nfl_text_functions_app()
    elif excel_func == "Date Functions":
        show_sec_date_functions_app()
    elif excel_func == "PMT Financial Function":
        show_financial_pmt_app()

elif choice == topics[1]:
    st.header("Statistics")
    analysis_tool = st.radio(
        "Choose a statistical analysis tool:",
        [
            "Descriptive Statistics", 
            "Histogram", 
            "Correlation", 
            "Regression"
        ]
    )

    show_data_analysis_app(selected_tool=analysis_tool)

elif choice == topics[2]:
    st.header("Structured Query Language")
    sql_lab = st.radio(
        "Choose a SQL practice:",
        [
            "SQL and SQLite practice 1.",
            "SQL Lab Slainte",
            "SQL Lab Slainte 2"
        ]
    )

    if sql_lab == "SQL and SQLite practice 1.":
        show_nfl_team_perf_app()
    elif sql_lab == "SQL Lab Slainte":
        # Call another function or display content
        pass
    elif sql_lab == "SQL Lab Slainte 2":
        # Call another function or display content
        pass

elif choice == topics[3]:
    st.header("Alteryx Cloud Application")
    st.markdown("""
#### **Alteryx Overview**

1. **Data Preparation**: Clean and transform data.
2. **Workflow Automation**: Streamline processes.
3. **Collaboration**: Share insights easily.
""")

elif choice == topics[4]:
    st.header("Python")
    python_option = st.radio(
        "Choose a Python practice:",
        [
            "Python Practice 1",
            "Python Practice 2",
            "Exercise Using Pandas"
        ]
    )
    if python_option == "Exercise Using Pandas":
        show_slainte_brewery_db_manager()
    elif python_option == "Python Practice 1":
        st.info("Python Practice 1 coming soon!")
    elif python_option == "Python Practice 2":
        st.info("Python Practice 2 coming soon!")

elif choice == topics[5]:  # or whatever index you want
    st.header("EU Superstore Analysis")
    st.markdown("""
#### **EU Superstore Dashboard**

1. **KPIs**: Sales, Profit, Customers.
2. **Map**: Sales by Country.
3. **Line Chart**: Sales by Month.
4. **Bar Chart**: Sales by Product.
""")
    show_eu_superstore_dashboard()
elif choice == topics[6]:
    st.header("Libayshuns Project")
    st.markdown("""
#### **Libayshuns Project Overview**

1. **Objective**: Improve customer engagement through personalized marketing.
2. **Data Sources**: CRM, Sales Data, Customer Feedback.
3. **Key Metrics**: Customer Retention, Sales Growth, Campaign ROI.
""")
    show_libayshuns_project()