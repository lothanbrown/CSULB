import streamlit as st
import pandas as pd
import sqlite3

def show_nfl_team_perf_app():
    # Upload
    st.title("NFL Team Performance Explorer")

    db_file = 'files/NFL_Team_Perf.db'
    csv_file = 'files/NFL_Team_Perf.csv'  # update if .txt

    @st.cache_data
    def get_data():
        conn = sqlite3.connect(db_file)
        df = pd.read_sql("SELECT * FROM NFL_Team_Perf", conn)
        conn.close()
        return df

    st.header("Browse Data")
    if st.button("Import CSV to SQLite"):
        # Import data
        df = pd.read_csv(csv_file)
        conn = sqlite3.connect(db_file)
        df.to_sql('NFL_Team_Perf', conn, if_exists='replace', index=False)
        conn.close()
        st.success("Data imported!")

    df = get_data()
    st.dataframe(df.head(10))

    st.markdown("---")
    st.header("Run Queries")

    query_options = [
        "Show Team, Revenue, and Winning Percentage 2019",
        "Show Team, Revenue, and Winning Percentage 2019 (sorted by Revenue)",
        "Show Team, Revenue, Points per Game Scored (Between 22-28)",
        "Show sum of revenue by state",
        "Show average revenue and player payroll by Division",
        "Show Divisions with avg payroll < 150",
        "Show all teams in Texas with revenue over 400M"
    ]

    sql_queries = [
        'SELECT Team, Revenue, "Winning Percentage 2019" FROM NFL_Team_Perf;',
        'SELECT Team, Revenue, "Winning Percentage 2019" FROM NFL_Team_Perf ORDER BY Revenue DESC;',
        'SELECT Team, Revenue, "Points per Game Scored" FROM NFL_Team_Perf WHERE "Points per Game Scored" BETWEEN 22 AND 28;',
        'SELECT State, SUM(Revenue) AS Total_Revenue FROM NFL_Team_Perf GROUP BY State;',
        'SELECT Division, AVG(Revenue) AS Avg_Revenue, AVG("Player Payroll") AS Avg_Player_Payroll FROM NFL_Team_Perf GROUP BY Division;',
        'SELECT Division, AVG(Revenue) AS Avg_Revenue, AVG("Player Payroll") AS Avg_Player_Payroll FROM NFL_Team_Perf GROUP BY Division HAVING AVG("Player Payroll") < 150;',
        "SELECT Team, State, Revenue FROM NFL_Team_Perf WHERE State = 'TX' AND Revenue > 400;"
    ]

    choice = st.selectbox("Select a query:", query_options)
    if st.button("Run Query"):
        query = sql_queries[query_options.index(choice)]
        conn = sqlite3.connect(db_file)
        result = pd.read_sql(query, conn)
        conn.close()
        st.dataframe(result)
        st.markdown("**Executed SQL:**")
        st.code(query, language="sql")

    st.markdown("---")
    st.subheader("Custom SQL Query")
    custom_query = st.text_area("Write your SQL query here:", height=100)
    if st.button("Run Custom Query"):
        conn = sqlite3.connect(db_file)
        try:
            result = pd.read_sql(custom_query, conn)
            st.dataframe(result)
        except Exception as e:
            st.error(f"Error: {e}")
        conn.close()