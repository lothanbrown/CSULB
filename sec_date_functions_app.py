import streamlit as st
import pandas as pd
from datetime import datetime

def show_sec_date_functions_app():
    st.header("📅 SEC Rules Date Functions")
    uploaded_file = st.file_uploader("Upload Excel Practice 1.xlsx", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file, sheet_name="SEC Rules")
        st.write("Original Data:")
        st.dataframe(df)

        # Copy Date to new column and change format to general (shows Excel serial)
        df['Date as Number'] = pd.to_datetime(df['Date']).map(lambda x: x.toordinal())

        # Today's date
        today = pd.Timestamp.today().normalize()
        df['Days Since Release'] = (today - pd.to_datetime(df['Date'])).dt.days

        df['Year'] = pd.to_datetime(df['Date']).dt.year
        df['Month'] = pd.to_datetime(df['Date']).dt.month
        df['Day of Week'] = pd.to_datetime(df['Date']).dt.dayofweek  # 0=Monday
        df['Day Name'] = pd.to_datetime(df['Date']).dt.day_name()

        st.write("With Date Functions Applied:")
        st.dataframe(df[['Date', 'Date as Number', 'Days Since Release', 'Year', 'Month', 'Day of Week', 'Day Name']])

        st.markdown("**Python Functions Executed:**")
        st.code(
            "df['Date as Number'] = pd.to_datetime(df['Date']).map(lambda x: x.toordinal())\n"
            "today = pd.Timestamp.today().normalize()\n"
            "df['Days Since Release'] = (today - pd.to_datetime(df['Date'])).dt.days\n"
            "df['Year'] = pd.to_datetime(df['Date']).dt.year\n"
            "df['Month'] = pd.to_datetime(df['Date']).dt.month\n"
            "df['Day of Week'] = pd.to_datetime(df['Date']).dt.dayofweek\n"
            "df['Day Name'] = pd.to_datetime(df['Date']).dt.day_name()",
            language="python"
        )

        st.markdown("**Equivalent Excel Formulas:**")
        st.code(
            'Date as Number: =VALUE(B3)\n'
            'Today\'s Date: =TODAY()\n'
            'Days Since Release: =TODAY()-B3\n'
            'Year: =YEAR(B3)\n'
            'Month: =MONTH(B3)\n'
            'Day of Week (number): =WEEKDAY(B3)\n'
            'Day Name: =TEXT(B3, "dddd")',
            language="excel"
        )