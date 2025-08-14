import streamlit as st
import pandas as pd

def show_nfl_text_functions_app():
    st.title("NFL Players Text Functions")

    uploaded_file = st.file_uploader("Upload Excel Practice 1.xlsx", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file, sheet_name="NFL Players")
        st.write("Original Data:")
        st.dataframe(df)

        # Assume full name is in column 'A' or named 'Full Name'
        if 'Full Name' in df.columns:
            name_col = 'Full Name'
        else:
            name_col = df.columns[0]

        # Text functions
        df['First Name'] = df[name_col].str.split().str[0]
        df['Last Name'] = df[name_col].str.split().str[-1]
        df['Last, First'] = df['Last Name'] + ", " + df['First Name']
        df['LAST, FIRST'] = df['Last, First'].str.upper()

        st.write("With Text Functions Applied:")
        st.dataframe(df[['First Name', 'Last Name', 'Last, First', 'LAST, FIRST']])

        st.markdown("**Python Functions Executed:**")
        st.code(
            "df['First Name'] = df[name_col].str.split().str[0]\n"
            "df['Last Name'] = df[name_col].str.split().str[-1]\n"
            "df['Last, First'] = df['Last Name'] + ', ' + df['First Name']\n"
            "df['LAST, FIRST'] = df['Last, First'].str.upper()",
            language="python"
        )

        st.markdown("**Equivalent Excel Formulas:**")
        st.code(
            'First Name: =TEXTBEFORE(A3, " ")\n'
            'Last Name: =TEXTAFTER(A3, " ")\n'
            'Last, First: =G3 & ", " & F3\n'
            'LAST, FIRST: =UPPER(H3)',
            language="excel"
        )

        # Text to columns (simulate)
        st.write("Text to Columns (First and Last Name):")
        split_names = df[name_col].str.split(expand=True)
        split_names.columns = ['First Name', 'Last Name']
        st.dataframe(split_names)

        st.markdown("**Excel Text to Columns:**")
        st.code(
            'Data > Data Tools > Text to Columns\n'
            'Delimited > Space',
            language="excel"
        )