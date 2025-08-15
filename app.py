import streamlit as st
from nfl_team_perf_app import show_nfl_team_perf_app
from nfl_text_functions_app import show_nfl_text_functions_app
from sec_date_functions_app import show_sec_date_functions_app
from financial_pmt_app import show_financial_pmt_app
from data_analysis_app import show_data_analysis_app
from slainte_brewery_db_manager import show_slainte_brewery_db_manager
from eu_superstore_dashboard import show_eu_superstore_dashboard
from libayshuns_project import show_libayshuns_project
from ai_chatbox_app import show_ai_chatbox

st.markdown(
    """
    <style>
    div[data-testid="stExpander"] {
        border: none;
        border-radius: 16px;
        box-shadow: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title='ACCT 605 Data Analytics Study Guide', layout='wide')

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    st.markdown("""
    <style>
    .logo-container {
        background: white;
        border-radius: 16px;
        padding: 40px 60px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.12);
        text-align: center;
        border: 3px solid #FFC72C;
        margin: 20px auto;
    }

    .icon-circle {
        width: 50px;
        height: 50px;
        background: #FFC72C;
        border-radius: 50%;
        margin: 0 auto 20px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        box-shadow: 0 4px 16px rgba(255, 199, 44, 0.3);
    }

    .course-code {
        font-size: 20px;
        font-weight: 800;
        color: #FFC72C;
        margin-bottom: 12px;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }

    .main-title {
        font-size: 28px;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 8px;
        line-height: 1.2;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }

    .divider {
        width: 80px;
        height: 3px;
        background: #FFC72C;
        margin: 20px auto;
        border-radius: 2px;
    }

    .subtitle {
        font-size: 16px;
        color: #7f8c8d;
        font-weight: 600;
        font-style: italic;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }
    </style>

    <div class="logo-container">
        <div class="icon-circle">📊</div>
        <div class="course-code">ACCT 605</div>
        <div class="main-title">Data Analytics in Accounting</div>
        <div class="divider"></div>
        <div class="subtitle">Welcome to the interactive practice guide!</div>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("**📖 How to Use This Guide**"):
        st.markdown("""
                    However you like! 🤷🏻

                    But here's my recommendation:

                    In a typical Snowflake work session, you might find yourself juggling various commands such as 
                    cloning a database and schema, creating new tables or views, rummaging through files on a stage, keeping tabs on Snowpipe, wrangling data through manual copying, insertion, or updating, etc, etc ... the list is long!

                    Now, keeping the precise syntax of all these commands at your fingertips, especially for the less-frequently-used ones, can be quite a challenge. 
                    I recommend keeping this cheat sheet open in a tab while you work. This way, you can swiftly refer to the provided code snippets and easily adapt them to your specific tasks. 
                    To keep things streamlit 🎈... sorry, I mean streamlined, I have removed options and arguments that are not frequently used in each command. 
                    However, keep in mind that I have cherry-picked the options based on my personal workflow experience which may not necessarily align with yours.     

                    Within each segment, there's a special treat ❄️: a bonus section with top tips to elevate your Snowflake skills.  
                    I suggest that whenever you are using a command for the first time, spend a few minutes reading the tips and hopefully pick up something new.
                    """)
        
        st.info("""
                This guide is not intended to be a replacement for the official [Snowflake documentation](https://docs.snowflake.com/) (which is fantastic by the way!). 
                    For a comprehensive reference of objects and methods, make sure to explore the official documentation.
                """)
        
        st.markdown("""
                    If you happen to spot any errors or have suggestions for improving the descriptions or tips, please don't hesitate to reach out to me directly [here](https://www.linkedin.com/in/siavash-yasini/), or open an [issue](https://github.com/syasini/snowflake_cheatsheet/issues/new) on the GitHub page. Your feedback is invaluable—and relied upon—in keeping this guide accurate and useful.

                    👈 Don't forget to check the sidebar for additional info and layout options!

                    Now, go build something awesome on Snowflake! 🚀

                    """)
    st.markdown("<br>", unsafe_allow_html=True)  
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
topics = [
    "Excel Practice",
    "Statistics",
    "SQL Practice",
    "Alteryx Cloud",
    "Python",
    "Tableau",
    "Libayshuns Project" 
]
choice = st.sidebar.selectbox("Choose a topic:", topics)
cols = st.columns(2)

if choice == topics[0]:
    with cols[0]:
        
        st.header("📊 Excel Practice")
        excel_func = st.radio(
            "Choose function for Excel Practice1:",
            [
                "Text Functions", 
                "Date Functions", 
                "PMT Financial Function"
            ]
        )
    with cols[1]:
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
show_ai_chatbox()