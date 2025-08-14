import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

def show_data_analysis_app(selected_tool=None):
    st.title("Excel Data Analysis Toolpak (Python Version)")

    uploaded_file = st.file_uploader("Upload Excel Practice 1-2.xlsx", type=["xlsx"])
    summary = ""
    if uploaded_file:
        xl = pd.ExcelFile(uploaded_file)
        sheet = st.selectbox("Select worksheet", xl.sheet_names)
        df = xl.parse(sheet)
        st.write("Data Preview:")
        st.dataframe(df)

        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        st.write("Numeric columns detected:", num_cols)
        cap_col = st.selectbox("Select Cap Space column", num_cols)
        pct_col = st.selectbox("Select PCT column", num_cols)

        if selected_tool == "Descriptive Statistics":
            st.subheader("Descriptive Statistics (Cap Space)")
            desc = df[cap_col].describe()
            st.write(desc)
            summary = (
                f"Descriptive statistics for {cap_col}:\n"
                f"Count: {desc['count']}\n"
                f"Mean: {desc['mean']:.2f}\n"
                f"Std: {desc['std']:.2f}\n"
                f"Min: {desc['min']:.2f}\n"
                f"25%: {desc['25%']:.2f}\n"
                f"Median: {desc['50%']:.2f}\n"
                f"75%: {desc['75%']:.2f}\n"
                f"Max: {desc['max']:.2f}"
            )
            st.markdown("**Python:**")
            st.code(f"df['{cap_col}'].describe()", language="python")
            st.markdown("**Excel:**")
            st.code(f"=DESCRIPTIVE STATISTICS({cap_col})", language="excel")

        elif selected_tool == "Histogram":
            st.subheader("Histogram (Cap Space)")
            fig, ax = plt.subplots()
            ax.hist(df[cap_col].dropna(), bins=10, edgecolor='black')
            ax.set_xlabel(cap_col)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
            summary = f"Histogram shows the distribution of {cap_col} values. Check for skewness, outliers, and the most common value ranges."
            st.markdown("**Python:**")
            st.code(f"plt.hist(df['{cap_col}'].dropna(), bins=10)", language="python")
            st.markdown("**Excel:**")
            st.code(f"=HISTOGRAM({cap_col})", language="excel")

        elif selected_tool == "Correlation":
            st.subheader("Correlation (Cap Space & PCT)")
            corr = df[[cap_col, pct_col]].corr().iloc[0,1]
            st.write(f"Correlation between {cap_col} and {pct_col}: **{corr:.3f}**")
            summary = (
                f"The correlation coefficient between {cap_col} and {pct_col} is {corr:.3f}.\n"
                "A value close to 1 or -1 indicates a strong linear relationship; a value near 0 indicates little or no linear relationship."
            )
            st.markdown("**Python:**")
            st.code(f"df[[{cap_col!r}, {pct_col!r}]].corr().iloc[0,1]", language="python")
            st.markdown("**Excel:**")
            st.code(f"=CORREL({cap_col} range, {pct_col} range)", language="excel")

        elif selected_tool == "Regression":
            st.subheader("Regression (Does PCT predict Cap Space?)")
            X = df[pct_col]
            y = df[cap_col]
            X = sm.add_constant(X)
            model = sm.OLS(y, X, missing='drop').fit()
            st.write(model.summary())
            r2 = model.rsquared
            pval = model.pvalues[1] if len(model.pvalues) > 1 else None
            coef = model.params[1] if len(model.params) > 1 else None
            summary = (
                f"Regression results:\n"
                f"R-squared: {r2:.3f}\n"
                f"Coefficient for {pct_col}: {coef:.3f}\n"
                f"P-value: {pval:.3g}\n"
                "A significant p-value (<0.05) suggests that PCT is a significant predictor of Cap Space."
            )
            st.markdown("**Python:**")
            st.code(
                f"import statsmodels.api as sm\n"
                f"X = sm.add_constant(df['{pct_col}'])\n"
                f"y = df['{cap_col}']\n"
                f"model = sm.OLS(y, X, missing='drop').fit()\n"
                f"model.summary()",
                language="python"
            )
            st.markdown("**Excel:**")
            st.code(
                "Use Data Analysis > Regression\n"
                "Y Range: Cap Space\n"
                "X Range: PCT",
                language="excel"
            )

        st.subheader("Summary")
        st.text_area("Summarize your results here:", value=summary, height=120)