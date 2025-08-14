import streamlit as st
import pandas as pd
import sqlite3
import io

def show_libayshuns_sql_analysis():
    st.header("Libayshuns SQL Analysis")

    sales_file = st.file_uploader("Upload Sales CSV", type=["csv"], key="sql_sales")
    master_inv_file = st.file_uploader("Upload Master Inventory CSV", type=["csv"], key="sql_master_inv")

    if sales_file and master_inv_file:
        # Load CSVs into DataFrames
        sales = pd.read_csv(sales_file)
        master_inv = pd.read_csv(master_inv_file)

        # Create SQLite DB in memory
        conn = sqlite3.connect(":memory:")
        sales.to_sql("sales", conn, index=False, if_exists="replace")
        master_inv.to_sql("master_inv", conn, index=False, if_exists="replace")

        # a. Summarize sales by store
        st.subheader("a. Sales by Store")
        query_sales_by_store = """
            SELECT Store, SUM(SalesDollars) AS TotalSales
            FROM sales
            GROUP BY Store
        """
        st.code(query_sales_by_store, language="sql")
        sales_by_store = pd.read_sql(query_sales_by_store, conn)
        st.dataframe(sales_by_store)

        # b. Join sales to master inventory on Item# to calculate cost of goods for each item
        st.subheader("b. Cost of Goods by Item (Sales JOIN Master Inventory)")
        query_cogs_by_item = """
            SELECT 
                s.Store,
                s."Item#",
                SUM(s.SalesQuantity) AS TotalSold,
                m.PurchasePrice,
                SUM(s.SalesQuantity * m.PurchasePrice) AS CostOfGoods
            FROM sales s
            JOIN master_inv m ON s."Item#" = m."Item#"
            GROUP BY s.Store, s."Item#"
        """
        st.code(query_cogs_by_item, language="sql")
        cogs_by_item = pd.read_sql(query_cogs_by_item, conn)
        st.dataframe(cogs_by_item)

        # c. Summarize cost of goods by store
        st.subheader("c. Cost of Goods by Store")
        query_cogs_by_store = """
            SELECT 
                Store,
                SUM(SalesQuantity * PurchasePrice) AS TotalCostOfGoods
            FROM sales
            JOIN master_inv ON sales."Item#" = master_inv."Item#"
            GROUP BY Store
        """
        st.code(query_cogs_by_store, language="sql")
        cogs_by_store = pd.read_sql(query_cogs_by_store, conn)
        st.dataframe(cogs_by_store)

        # d. Export summary CSVs
        st.subheader("d. Export Summary CSVs")
        csv1 = sales_by_store.to_csv(index=False).encode('utf-8')
        st.download_button("Download Sales by Store CSV", csv1, "sales_by_store.csv", "text/csv")
        csv2 = cogs_by_store.to_csv(index=False).encode('utf-8')
        st.download_button("Download Cost of Goods by Store CSV", csv2, "cogs_by_store.csv", "text/csv")

        conn.close()
    else:
        st.info("Upload both Sales and Master Inventory CSVs to begin SQL analysis.")