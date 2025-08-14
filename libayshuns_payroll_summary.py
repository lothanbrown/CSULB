import streamlit as st
import pandas as pd

def show_libayshuns_payroll_summary():
    st.header("Libayshuns Payroll Summary (Python & Pandas)")

    payroll_file = st.file_uploader("Upload Payroll CSV", type=["csv"], key="payroll_summary")
    if payroll_file:
        payroll = pd.read_csv(payroll_file)

        # Calculate total payroll payables for each row
        payroll['TotalPayrollPayables'] = (
            payroll['FedTax'] + payroll['StTax'] +
            payroll['FICA'] + payroll['EmFica'] +
            payroll['Medicare'] + payroll['EmMedicare']
        )

        # Summarize by store
        summary = payroll.groupby('Store').agg(
            TotalPay=('SalaryWagesPerPP', 'sum'),
            TotalPayrollPayables=('TotalPayrollPayables', 'sum')
        ).reset_index()

        st.dataframe(summary)

        # Export to CSV
        csv = summary.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download Payroll Summary CSV",
            csv,
            "payroll_summary_by_store.csv",
            "text/csv"
        )

        st.code(
            """
payroll['TotalPayrollPayables'] = (
    payroll['FedTax'] + payroll['StTax'] +
    payroll['FICA'] + payroll['EmFica'] +
    payroll['Medicare'] + payroll['EmMedicare']
)

summary = payroll.groupby('Store').agg(
    TotalPay=('SalaryWagesPerPP', 'sum'),
    TotalPayrollPayables=('TotalPayrollPayables', 'sum')
).reset_index()
            """, language="python"
        )
    else:
        st.info("Upload the Payroll CSV to see the summary.")