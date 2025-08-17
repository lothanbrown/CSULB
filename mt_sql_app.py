import streamlit as st
import pandas as pd
import sqlite3
import os

def show_sql_app():
    st.title("SQL Automation: Johnson & Johnson (JNJ)")

    st.markdown("""
    **Instructions:**  
    Upload your cleaned company and industry CSV files.  
    This app will create a SQLite database, import the data, run the required SQL, and export the results.
    """)

    company_csv = st.file_uploader("Upload Cleaned Company Data (CSV)", type=["csv"])
    industry_csv = st.file_uploader("Upload Cleaned Industry Data (CSV)", type=["csv"])

    if company_csv and industry_csv:
        # Read CSVs
        company_df = pd.read_csv(company_csv)
        industry_df = pd.read_csv(industry_csv)

        # Create SQLite DB
        db_name = "files/JNJ.db"
        conn = sqlite3.connect(db_name)

        # Import data to DB
        company_table = "JNJData"
        industry_table = "PharmaData"
        company_df.to_sql(company_table, conn, if_exists="replace", index=False)
        industry_df.to_sql(industry_table, conn, if_exists="replace", index=False)

        st.success(f"Database {db_name} created and tables imported.")

        # Required ratios
        ratios = [
            "AssetTurn", "GrossProfitMargin", "NetProfitMargin", "ROA",
            "ROE", "InventoryTurn", "AssetToEquity", "QuickRatio"
        ]
        ratio_select = ", ".join([f"{company_table}.{r} as company_{r}, {industry_table}.{r} as industry_{r}" for r in ratios])
        diff_select = ", ".join([f"({company_table}.{r} - {industry_table}.{r}) as diff_{r}" for r in ratios])
        avg_diff_select = ", ".join([f"AVG({company_table}.{r} - {industry_table}.{r}) as avg_diff_{r}" for r in ratios])

        # 1. Join and export
        query1 = f"""
        SELECT {company_table}.*, 
            {', '.join([f'{industry_table}.{r} as industry_{r}' for r in ratios])}
        FROM {company_table}
        JOIN {industry_table}
        ON {company_table}.Calendar_Year = {industry_table}.Calendar_Year
        """
        st.markdown("**SQL Query 1: Join company and industry data**")
        st.code(query1, language="sql")
        df1 = pd.read_sql_query(query1, conn)
        st.subheader("Company with Industry Data")
        st.dataframe(df1)
        df1.to_csv("files/JNJ-with-industry.csv", index=False)
        st.download_button("Download JNJ-with-industry.csv", df1.to_csv(index=False).encode('utf-8'), "JNJ-with-industry.csv", "text/csv")

        # 2. Differences and export
        query2 = f"""
        SELECT {company_table}.Company, {company_table}.Calendar_Year, {diff_select}
        FROM {company_table}
        JOIN {industry_table}
        ON {company_table}.Calendar_Year = {industry_table}.Calendar_Year
        """
        st.markdown("**SQL Query 2: Compute differences between company and industry ratios**")
        st.code(query2, language="sql")
        df2 = pd.read_sql_query(query2, conn)
        st.subheader("Differences in Ratios")
        st.dataframe(df2)
        df2.to_csv("files/JNJ-differences.csv", index=False)
        st.download_button("Download JNJ-differences.csv", df2.to_csv(index=False).encode('utf-8'), "JNJ-differences.csv", "text/csv")

        # 3. Average differences and export
        query3 = f"""
        SELECT {avg_diff_select}
        FROM {company_table}
        JOIN {industry_table}
        ON {company_table}.Calendar_Year = {industry_table}.Calendar_Year
        """
        st.markdown("**SQL Query 3: Compute average differences (one row)**")
        st.code(query3, language="sql")
        df3 = pd.read_sql_query(query3, conn)
        st.subheader("Average Differences (One Row)")
        st.dataframe(df3)
        df3.to_csv("files/JNJ-summary-differences.csv", index=False)
        st.download_button("Download JNJ-summary-differences.csv", df3.to_csv(index=False).encode('utf-8'), "JNJ-summary-differences.csv", "text/csv")

        # Save DB file for download
        with open(db_name, "rb") as f:
            st.download_button("Download SQLite DB (JNJ.db)", f, db_name, "application/octet-stream")

        st.info("Remember to submit your SQLite project and DB files as required.")

        conn.close()
    else:
        st.info("Please upload both cleaned CSV files to proceed.")