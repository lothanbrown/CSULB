import streamlit as st
import pandas as pd
import sqlite3

def show_libayshuns_questions():
    st.header("Project Questions & Answers")

    # Upload all relevant files once
    sales_file = st.file_uploader("Upload Sales CSV", type=["csv"], key="q_sales")
    master_inv_file = st.file_uploader("Upload Master Inventory CSV", type=["csv"], key="q_master_inv")
    payroll_file = st.file_uploader("Upload Payroll CSV", type=["csv"], key="q_payroll")
    begin_inv_file = st.file_uploader("Upload Beginning Inventory CSV", type=["csv"], key="q_begin_inv")
    end_inv_file = st.file_uploader("Upload Ending Inventory CSV", type=["csv"], key="q_end_inv")

    # Load dataframes if files are uploaded
    sales, master_inv, payroll, begin_inv, end_inv = None, None, None, None, None
    if sales_file:
        try:
            sales = pd.read_csv(sales_file, parse_dates=["SalesDate"])
        except Exception as e:
            st.error(f"Error loading Sales CSV: {e}")
    if master_inv_file:
        master_inv = pd.read_csv(master_inv_file)
    if payroll_file:
        payroll = pd.read_csv(payroll_file)
    if begin_inv_file:
        begin_inv = pd.read_csv(begin_inv_file)
    if end_inv_file:
        end_inv = pd.read_csv(end_inv_file)

    # 1. Revenue by store and quarter
    with st.expander("1. What was the revenue for each store and total revenue for each quarter and for the entire fiscal year?"):
        if sales is not None and not sales.empty:
            conn = sqlite3.connect(":memory:")
            sales.to_sql("sales", conn, index=False, if_exists="replace")
            query = """
                SELECT
                    Store,
                    strftime('%Y', SalesDate) AS Year,
                    ((cast(strftime('%m', SalesDate) as integer) - 1) / 3 + 1) AS Quarter,
                    SUM(SalesDollars) AS Revenue
                FROM sales
                GROUP BY Store, Year, Quarter
                ORDER BY Store, Year, Quarter;
            """
            st.code(query, language="sql")
            revenue_by_store = pd.read_sql(query, conn)
            st.dataframe(revenue_by_store)

            query_total = """
                SELECT
                    SUM(SalesDollars) AS TotalRevenue
                FROM sales
                WHERE SalesDate BETWEEN '2023-10-01' AND '2024-09-30';
            """
            st.code(query_total, language="sql")
            total_revenue = pd.read_sql(query_total, conn)
            st.write("**Total Revenue for Fiscal Year (Q4 2023 - Q3 2024):**")
            st.dataframe(total_revenue)
            conn.close()
        else:
            st.info("Upload the Sales CSV to view revenue analysis.")

    # 2. Cost of goods and gross profit margin
    with st.expander("2. What was the cost of goods and gross profit margin for each store and in total for each quarter and for the entire fiscal year?"):
        if sales is not None and master_inv is not None and not sales.empty and not master_inv.empty:
            conn = sqlite3.connect(":memory:")
            sales.to_sql("sales", conn, index=False, if_exists="replace")
            master_inv.to_sql("master_inv", conn, index=False, if_exists="replace")
            query = """
                SELECT
                    s.Store,
                    strftime('%Y', s.SalesDate) AS Year,
                    ((cast(strftime('%m', s.SalesDate) as integer) - 1) / 3 + 1) AS Quarter,
                    SUM(s.SalesDollars) AS Revenue,
                    SUM(s.SalesQuantity * m.PurchasePrice) AS CostOfGoods,
                    SUM(s.SalesDollars) - SUM(s.SalesQuantity * m.PurchasePrice) AS GrossProfit
                FROM sales s
                JOIN master_inv m ON s."Item#" = m."Item#"
                GROUP BY s.Store, Year, Quarter
                ORDER BY s.Store, Year, Quarter;
            """
            st.code(query, language="sql")
            cogs_margin = pd.read_sql(query, conn)
            st.dataframe(cogs_margin)
            conn.close()
        else:
            st.info("Upload both Sales and Master Inventory CSVs to view cost of goods and gross profit margin.")

    # 3. Payroll expenses by store and in total
    with st.expander("3. What were the payroll expenses by store and in total for each quarter and for the entire fiscal year?"):
        if payroll is not None and not payroll.empty:
            payroll['PayPeriod'] = pd.to_datetime(payroll['PayPeriod'])
            payroll['Year'] = payroll['PayPeriod'].dt.year
            payroll['Quarter'] = payroll['PayPeriod'].dt.quarter
            payroll['TotalPayrollPayables'] = (
                payroll['FedTax'] + payroll['StTax'] +
                payroll['FICA'] + payroll['EmFica'] +
                payroll['Medicare'] + payroll['EmMedicare']
            )
            summary = payroll.groupby(['Store', 'Year', 'Quarter']).agg(
                TotalPay=('SalaryWagesPerPP', 'sum'),
                TotalPayrollPayables=('TotalPayrollPayables', 'sum')
            ).reset_index()
            st.dataframe(summary)
        else:
            st.info("Upload the Payroll CSV to view payroll expenses.")

    # 4. Inventory difference
    with st.expander("4. What was the difference between calculated and actual ending inventory? What contributed to the difference, if any?"):
        if begin_inv is not None and end_inv is not None and not begin_inv.empty and not end_inv.empty:
            merged = pd.merge(begin_inv, end_inv, on=["InventoryId", "Store", "Item#"], suffixes=('_begin', '_end'))
            merged['Difference'] = merged['onHand_end'] - merged['onHand_begin']
            st.dataframe(merged[['Store', 'Item#', 'onHand_begin', 'onHand_end', 'Difference']])
        else:
            st.info("Upload Beginning and Ending Inventory CSVs to compare inventories.")

    # 5. Best sellers in master inventory
    with st.expander("5. Which items in the master inventory list were best sellers?"):
        if sales is not None and not sales.empty:
            best_sellers = sales.groupby('Item#')['SalesQuantity'].sum().reset_index().sort_values('SalesQuantity', ascending=False)
            st.dataframe(best_sellers.head(10))
        else:
            st.info("Upload the Sales CSV to view best sellers.")

    # 6. Difference in best sellers among stores
    with st.expander("6. Was there a difference in the inventory best sellers among stores?"):
        if sales is not None and not sales.empty:
            best_by_store = sales.groupby(['Store', 'Item#'])['SalesQuantity'].sum().reset_index()
            st.dataframe(best_by_store.sort_values(['Store', 'SalesQuantity'], ascending=[True, False]).groupby('Store').head(5))
        else:
            st.info("Upload the Sales CSV to compare best sellers among stores.")