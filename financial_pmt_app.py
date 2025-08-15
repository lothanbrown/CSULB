import streamlit as st
import pandas as pd
import numpy_financial as npf

def show_financial_pmt_app():
    st.header("💰 PMT Financial Function")
    uploaded_file = st.file_uploader("Upload Excel Practice 1.xlsx", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file, sheet_name="Financial")
        st.write("Original Data:")
        st.dataframe(df)

        # Loan parameters
        loan_amount = 35000
        years = 5
        nper = years * 12

        # Get rates from the DataFrame or use example rates
        if 'Rate' in df.columns:
            rates = df['Rate'].dropna().tolist()
        else:
            rates = [0.03, 0.04, 0.05, 0.06, 0.07]

        # Calculate payments for each rate
        payments = []
        for rate in rates:
            monthly_rate = rate / 12
            pmt = npf.pmt(monthly_rate, nper, -loan_amount)
            payments.append(pmt)

        # Create a new DataFrame for results
        results_df = pd.DataFrame({
            'Rate': rates,
            'Monthly Payment': payments
        })

        st.write("Monthly Payments for Each Rate:")
        st.dataframe(results_df)

        # Show the function/formula used
        st.markdown("**Function Executed:**")
        st.code(
            "pmt = npf.pmt(monthly_rate, nper, -loan_amount)\n"
            "# monthly_rate = rate / 12\n"
            "# nper = years * 12\n"
            "# loan_amount = 35000",
            language="python"
        )
        st.markdown("**Equivalent Excel Formula:**")
        st.code(
            "=PMT(rate/12, years*12, -loan_amount)",
            language="excel"
        )