import streamlit as st
import pandas as pd

def show_libayshuns_income_statement():
    st.header("Libayshuns Income Statement Builder (Python & Pandas)")

    sales_file = st.file_uploader("Upload Sales by Store CSV", type=["csv"], key="income_sales")
    cogs_file = st.file_uploader("Upload Cost of Goods by Store CSV", type=["csv"], key="income_cogs")
    payroll_file = st.file_uploader("Upload Payroll Summary by Store CSV", type=["csv"], key="income_payroll")

    if sales_file and cogs_file and payroll_file:
        sales = pd.read_csv(sales_file)
        cogs = pd.read_csv(cogs_file)
        payroll = pd.read_csv(payroll_file)

        df = sales.merge(cogs, on="Store", how="outer").merge(payroll, on="Store", how="outer")
        df = df.fillna(0)
        df["GrossProfit"] = df["TotalSales"] - df["TotalCostOfGoods"]
        df["NetIncome"] = df["GrossProfit"] - df["TotalPay"]
        df = df[["Store", "TotalSales", "TotalCostOfGoods", "GrossProfit", "TotalPay", "NetIncome"]]
        total_row = pd.DataFrame({
            "Store": ["Total"],
            "TotalSales": [df["TotalSales"].sum()],
            "TotalCostOfGoods": [df["TotalCostOfGoods"].sum()],
            "GrossProfit": [df["GrossProfit"].sum()],
            "TotalPay": [df["TotalPay"].sum()],
            "NetIncome": [df["NetIncome"].sum()]
        })
        df = pd.concat([df, total_row], ignore_index=True)

        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download Income Statement CSV",
            csv,
            "income_statement_by_store.csv",
            "text/csv"
        )

        st.code(
            """
df = sales.merge(cogs, on="Store", how="outer").merge(payroll, on="Store", how="outer")
df = df.fillna(0)
df["GrossProfit"] = df["TotalSales"] - df["TotalCostOfGoods"]
df["NetIncome"] = df["GrossProfit"] - df["TotalPay"]
df = df[["Store", "TotalSales", "TotalCostOfGoods", "GrossProfit", "TotalPay", "NetIncome"]]
total_row = pd.DataFrame({
    "Store": ["Total"],
    "TotalSales": [df["TotalSales"].sum()],
    "TotalCostOfGoods": [df["TotalCostOfGoods"].sum()],
    "GrossProfit": [df["GrossProfit"].sum()],
    "TotalPay": [df["TotalPay"].sum()],
    "NetIncome": [df["NetIncome"].sum()]
})
df = pd.concat([df, total_row], ignore_index=True)
            """, language="python"
        )
    else:
        st.info("Upload all three summary CSVs to build the income statement.")