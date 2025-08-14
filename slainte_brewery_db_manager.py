import streamlit as st
import pandas as pd

def show_slainte_brewery_db_manager():
    st.title("Slainte Brewery Data Explorer (Pandas as a Database Manager)")

    uploaded_file = st.file_uploader("Upload 'Slainte Brewery Data for Python.xlsx'", type=["xlsx"])
    if uploaded_file:
        # Sheet selection and loading
        xl = pd.ExcelFile(uploaded_file)
        st.write("Worksheets found:", xl.sheet_names)

        # Read Customers and Sales Items
        s_cust = xl.parse("Customers")
        s_sales = xl.parse("Sales Items")

        st.subheader("1. First 5 Rows of Each Sheet")
        st.write("**Customers:**")
        st.dataframe(s_cust.head())
        st.write("**Sales Items:**")
        st.dataframe(s_sales.head())

        st.subheader("2. Summary Statistics")
        st.write("**Customers:**")
        st.dataframe(s_cust.describe())
        st.write("**Sales Items:**")
        st.dataframe(s_sales.describe())

        st.subheader("3. Numeric Columns & Correlations (Sales Items)")
        numeric_columns = s_sales.select_dtypes(include=['int', 'float']).columns
        st.write("Numeric columns:", list(numeric_columns))
        st.write("Correlation matrix:")
        st.dataframe(s_sales[numeric_columns].corr())

        st.subheader("4. Filter Sales Items by Product Code")
        product_codes = s_sales['Product_Code'].unique()
        selected_code = st.selectbox("Select Product Code to filter:", product_codes)
        filtered_df = s_sales[s_sales['Product_Code'] == selected_code]
        st.dataframe(filtered_df)

        st.subheader("5. Merge Sales Items with Customers (SQL JOIN)")
        cust_sales = pd.merge(s_sales, s_cust, on='Customer_ID', how='left')
        st.dataframe(cust_sales.head())

        st.subheader("6. Group By / Pivot Table")
        st.write("**Sum of Amount by Customer State:**")
        grouped_state = cust_sales.groupby('Customer_State').agg({'Amount': ['sum']})
        st.dataframe(grouped_state)

        st.write("**Sum of Amount by Product Code:**")
        grouped_product = cust_sales.groupby('Product_Code').agg({'Amount': ['sum']})
        st.dataframe(grouped_product)

        st.subheader("7. Download Results")
        # Write multiple DataFrames to Excel in memory
        import io
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            s_cust.to_excel(writer, sheet_name="Customers")
            s_sales.to_excel(writer, sheet_name="Sales Items")
            grouped_state.to_excel(writer, sheet_name="Grouped State")
            grouped_product.to_excel(writer, sheet_name="Grouped Product")
            cust_sales.to_excel(writer, sheet_name="Merged")
        output.seek(0)
        st.download_button(
            label="Download All Results as Excel",
            data=output,
            file_name="Slainte_Brewery_All_Results.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.info("Please upload the Excel file to begin.")