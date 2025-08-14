import streamlit as st
from nfl_team_perf_app import show_nfl_team_perf_app
from nfl_text_functions_app import show_nfl_text_functions_app
from sec_date_functions_app import show_sec_date_functions_app
from financial_pmt_app import show_financial_pmt_app
from data_analysis_app import show_data_analysis_app

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
        background-color: #ffffff;
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
    "Tableau"
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
    st.markdown("""
#### **Python for Data Analysis**

1. **Pandas**: Data manipulation.
2. **NumPy**: Numerical computing.
3. **Matplotlib**: Data visualization.
""")

elif choice == topics[5]:
    st.header("Tableau")
    st.markdown("""
#### **Tableau Essentials**

1. **Data Connections**: Connect to various data sources.
2. **Visualizations**: Create interactive dashboards.
3. **Sharing Insights**: Publish and share reports.
""")