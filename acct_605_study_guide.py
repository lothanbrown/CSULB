import streamlit as st
from nfl_team_perf_app import show_nfl_team_perf_app

st.set_page_config(page_title='ACCT 605 Data Analytics Study Guide', layout='wide')

st.title("ACCT 605-01: Data Analytics in Accounting")
st.markdown("""
Welcome to your interactive study guide! Use the sidebar to navigate between topics.
---
""")

topics = [
    "Excel Review",
    "Statistics",
    "Structured Query Language",
    "Alteryx Cloud Application",
    "Python",
    "Tableau"
]
choice = st.sidebar.selectbox("Choose a topic:", topics)

if choice == topics[0]:
    st.header("Excel Review")
    st.markdown("""
#### **Excel Functions**

1. **SUMIFS**: Conditional sum.
2. **VLOOKUP**: Vertical lookup.
3. **Pivot Tables**: Data summarization.
""")

elif choice == topics[1]:
    st.header("Statistics")
    st.markdown("""
#### **Key Concepts**

1. **Mean**: Average value.
2. **Median**: Middle value.
3. **Standard Deviation**: Measure of variability.
""")

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