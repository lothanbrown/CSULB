import streamlit as st
import pandas as pd
import os
import io

def show_company_files():
    st.title("Company and Data Assignment: Johnson & Johnson (JNJ)")

    st.markdown("""
    **Instructions:**  
    Upload the company data file (`JNJ Data.xlsx`) and the industry average file (`Pharma Data.xlsx`).  
    The app will display the data, convert percentage columns to numbers, and allow you to download both CSV and Excel versions.
    """)

    # File uploaders
    company_file = st.file_uploader("Upload Johnson & Johnson Data File (JNJ Data.xlsx)", type=["xlsx"])
    industry_file = st.file_uploader("Upload Industry Average File (Pharma Data.xlsx)", type=["xlsx"])

    def convert_percentages(df):
        # Convert percentage columns to numeric (e.g., 10% → 0.10)
        for col in df.columns:
            if df[col].dtype == object and df[col].str.contains('%').any():
                df[col] = df[col].str.replace('%', '').astype(float) / 100
        return df

    if company_file and industry_file:
        # Read Excel files
        company_df = pd.read_excel(company_file)
        industry_df = pd.read_excel(industry_file)

        st.subheader("Company Data (Original)")
        st.dataframe(company_df)

        st.subheader("Industry Average Data (Original)")
        st.dataframe(industry_df)

        # Convert percentages
        company_df_clean = convert_percentages(company_df.copy())
        industry_df_clean = convert_percentages(industry_df.copy())

        st.subheader("Company Data (Percentages Converted)")
        st.dataframe(company_df_clean)

        st.subheader("Industry Average Data (Percentages Converted)")
        st.dataframe(industry_df_clean)

        # Save to CSV and Excel
        company_csv = company_df_clean.to_csv(index=False).encode('utf-8')
        industry_csv = industry_df_clean.to_csv(index=False).encode('utf-8')

        output = io.BytesIO()
        company_df_clean.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)  # Move to the beginning of the buffer

        st.download_button("Download Cleaned Company Data (CSV)", company_csv, "JNJ_Data_Clean.csv", "text/csv")
        st.download_button(
            label="Download Cleaned Company Data (Excel)",
            data=output,
            file_name="JNJ_Data_Clean.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        st.download_button("Download Cleaned Industry Data (CSV)", industry_csv, "Pharma_Data_Clean.csv", "text/csv")
        st.download_button("Download Cleaned Industry Data (Excel)", industry_file, "Pharma_Data_Clean.xlsx")

        st.markdown("### Assumptions Made")
        st.text_area("List any assumptions you made here:", height=150)

    else:
        st.info("Please upload both the company and industry average Excel files to proceed.")