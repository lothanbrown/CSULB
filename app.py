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
from utils import st_code_block, make_tabs
from app_markdown_blocks import (
    get_button_css, get_expander_css, get_file_uploader_css, get_logo_html, get_how_to_use, get_how_to_use_info, get_how_to_use_feedback,
    get_excel_text_takeaways, get_excel_date_takeaways, get_excel_pmt_takeaways,
    get_alteryx_overview, get_eu_superstore_overview, get_libayshuns_overview, get_statistics_correlation_regression_col1, get_statistics_descriptive_col1, get_statistics_histogram_col1
)
st.markdown(get_button_css(), unsafe_allow_html=True)
st.markdown(get_expander_css(), unsafe_allow_html=True)
st.markdown(get_file_uploader_css(), unsafe_allow_html=True)


for _ in range(3):
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image("files/logo.png", use_container_width=True)  # Add logo to the top of the sidebar
st.sidebar.markdown("<br>", unsafe_allow_html=True)


st.set_page_config(page_title='ACCT 605 Data Analytics Study Guide', layout='wide')

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    st.markdown(get_logo_html(), unsafe_allow_html=True)
    with st.expander("**📖 How to Use This Guide**"):
        st.markdown(get_how_to_use())
        st.info(get_how_to_use_info())
        st.markdown(get_how_to_use_feedback())
    for _ in range(5):
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



if choice == topics[0]:
    st.header("📊 Excel Practice")
    text_tab, date_tab, pmt_tab = make_tabs(["TEXT FUNCTIONS", "DATE FUNCTIONS", "FINANCIAL FUNCTIONS"])

    with text_tab:
        col1, spacer, col2 = st.columns([0.4, 0.05, 0.55])
        with col1:
            st.markdown(get_excel_text_takeaways())
        with col2:
            show_nfl_text_functions_app()
    with date_tab:
        col1, spacer, col2 = st.columns([0.4, 0.05, 0.55])
        with col1:
            st.markdown(get_excel_date_takeaways())
        with col2:
            show_sec_date_functions_app()
    with pmt_tab:
        col1, spacer, col2 = st.columns([0.4, 0.05, 0.55])
        with col1:
            st.markdown(get_excel_pmt_takeaways())
        with col2:
            show_financial_pmt_app()
elif choice == topics[1]:
    st.header("🧠 Statistics")
    tab_1, tab_2, tab_3, tab_4 = make_tabs(["DESCRIPTIVE", "HISTOGRAM", "CORRELATION", "REGRESSION"])
    with tab_1:
        col1, spacer, col2 = st.columns([0.4, 0.05, 0.55])
        with col1:
            st.markdown(get_statistics_descriptive_col1())
        with col2:
            show_data_analysis_app(selected_tool="Descriptive Statistics")
    with tab_2:
        col1, spacer, col2 = st.columns([0.4, 0.05, 0.55])
        with col1:
            st.markdown(get_statistics_histogram_col1())
        with col2:
            show_data_analysis_app(selected_tool="Histogram")
    with tab_3:
        col1, spacer, col2 = st.columns([0.4, 0.05, 0.55])
        with col1:
            st.markdown(get_statistics_correlation_regression_col1())
        with col2:
           show_data_analysis_app(selected_tool= "Correlation")
    with tab_4:
        col1, spacer, col2 = st.columns([0.4, 0.05, 0.55])
        with col1:
            st.markdown(get_statistics_correlation_regression_col1())
        with col2:
           show_data_analysis_app(selected_tool= "Regression")
elif choice == topics[2]:
    st.header("🗃️ Structured Query Language")
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
    st.header("☁️ Alteryx Cloud Application")
    st.markdown(get_alteryx_overview())

elif choice == topics[4]:
    st.header("🐍 Python")
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
    st.markdown(get_eu_superstore_overview())
    show_eu_superstore_dashboard()
elif choice == topics[6]:
    st.header("🤝 Libayshuns Project")
    st.markdown(get_libayshuns_overview())
    show_libayshuns_project()
# show_ai_chatbox()