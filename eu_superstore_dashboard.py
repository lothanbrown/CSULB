import streamlit as st
import pandas as pd
import plotly.express as px

def show_eu_superstore_dashboard():
    st.title("EU Superstore Dashboard (Python Version)")

    uploaded_file = st.file_uploader("Upload 'Sample - EU Superstore.xlsx'", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file, sheet_name="Orders", parse_dates=["Order Date"])
        df['Year'] = df['Order Date'].dt.year
        df_2022 = df[df['Year'] == 2022]

        st.header("KPIs for 2022")
        col1, col2, col3 = st.columns(3)
        col1.metric("Sales", f"${df_2022['Sales'].sum():,.0f}")
        col2.metric("Profit", f"${df_2022['Profit'].sum():,.0f}")
        col3.metric("# of Customers", df_2022['Customer ID'].nunique())

        st.markdown("---")
        st.header("Sales by Country (Map)")
        country_sales = df_2022.groupby("Country/Region")["Sales"].sum().reset_index()
        fig_map = px.choropleth(
            country_sales,
            locations="Country/Region",
            locationmode="country names",
            color="Sales",
            color_continuous_scale="Blues",
            title="Sales by Country"
        )
        st.plotly_chart(fig_map, use_container_width=True)

        st.markdown("---")
        st.header("Sales by Month (Line Chart)")
        df_2022['Month'] = df_2022['Order Date'].dt.to_period('M').astype(str)
        monthly_sales = df_2022.groupby('Month')['Sales'].sum().reset_index()
        fig_line = px.line(monthly_sales, x='Month', y='Sales', markers=True, title="Sales by Month")
        st.plotly_chart(fig_line, use_container_width=True)

        st.markdown("---")
        st.header("Sales by Product (Bar Chart)")
        sales_by_product = df_2022.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).reset_index()
        avg_sales = sales_by_product['Sales'].mean()
        sales_by_product['Above Ave Sales'] = sales_by_product['Sales'] >= avg_sales
        fig_bar = px.bar(
            sales_by_product,
            x='Sales',
            y='Sub-Category',
            orientation='h',
            color='Above Ave Sales',
            color_discrete_map={True: 'blue', False: 'lightgray'},
            title="Sales by Product"
        )
        fig_bar.add_shape(
            type="line",
            x0=avg_sales, x1=avg_sales,
            y0=-0.5, y1=len(sales_by_product)-0.5,
            line=dict(color="red", dash="dash"),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("---")
        st.header("Download Filtered Data")
        csv = df_2022.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download 2022 Data as CSV",
            data=csv,
            file_name='EU_Superstore_2022.csv',
            mime='text/csv'
        )
    else:
        st.info("Please upload the Excel file to begin.")