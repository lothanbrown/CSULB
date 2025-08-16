def get_statistics_correlation_regression_col1():
    return '''
#### **Takeaways**
- **Purpose:**  
    - Correlation quantifies the linear association between two variables (for example, does more experience correlate with more rushing yards?).
    - Regression evaluates the predictive capability of one variable upon another and quantifies the strength and form of their relationship.
- **Preparation:**  
    - Place the variables of interest adjacent on your worksheet (e.g., copy ‘Yrs Experience’ and ‘Rushing Yards’ side by side).
- **Correlation Analysis:**  
    - Go to Data > Data Analysis > Correlation, select both columns (with labels), specify output range.
    - Output is a correlation matrix (values range -1 to 1); closer to 1 indicates strong positive relationship, closer to -1 indicates strong negative, near 0 suggests little/no linear relationship.
- **Regression Analysis:**  
    - Go to Data > Data Analysis > Regression.
    - Select ‘Rushing Yards’ as the dependent variable (Input Y), and ‘Years of Experience’ as the independent variable (Input X).
    - Mark the box for labels, designate output, and choose ‘Line Fit Plots’ for visualization.
    - Examine ‘Summary Output’ for Multiple R (overall correlation in regression), coefficient values, t-statistic (measures reliability of predictor), and P-value (statistical significance test).
    - **Interpreting Output:**  
        - If the coefficient for years of experience has a high P-value (e.g., 0.26), this indicates statistical insignificance; years of experience does not reliably predict rushing yards.
        - Multiple R gives an idea of total correlation from the regression; if familiar, it matches simple correlation coefficient for one predictor.
    - Encourages critical assessment rather than assuming all relationships are meaningful.
    '''
def get_statistics_histogram_col1():
    return '''
#### **Takeaways**
- **Purpose:** A histogram visually depicts the frequency distribution of a variable within selected bins, helping you identify patterns such as skewness, modality, and concentration of values.
- **Process:**  
    - Access Data > Data Analysis > Histogram, select the 'Cash' column as your input range, skip bin range if unsure, and choose to output to a new worksheet.
    - Tick options for Pareto (ranking bins by frequency), Cumulative Percentage (shows accumulation of frequencies), and Chart Output (visualizes results).
- **Analysis:**  
    - Excel automatically determines a bin count unless specified otherwise. The highest frequency bin reveals the range most common among participants.
    - Reviewing histograms helps pinpoint whether data is evenly spread, clustered, or contains significant outliers.
    '''
def get_statistics_descriptive_col1():
    return '''
#### **Takeaways**
- **Purpose:** To summarize key characteristics of dataset columns such as average, spread, and extremities (e.g., mean, median, mode, standard deviation, minimum, maximum).
- **Process:**  
    - Go to Data > Data Analysis > Descriptive Statistics.
    - Specify your input range (e.g., PCT data Q1:Q33), indicate if labels are present, choose your output location, and check 'Summary statistics.'
    - The provided output consolidates several calculations into a summary, eliminating the need for manual one-by-one computations.
    - **Interpretation:** The descriptive statistics help you quickly gauge the central tendency, variability, and shape of the data distribution, setting a foundation for further analysis.
    - For example, you can see if the data is skewed or has outliers by comparing the mean and median, and the standard deviation tells you how spread out values are.
    - Repeating the process for 'Cash' pay column produces a similar automated summary.
    '''
def get_expander_css():
    return '''
    <style>
    div[data-testid="stExpander"] {
        border: none;
        border-radius: 16px;
        box-shadow: none;
    }
    </style>
    '''

def get_logo_html():
    return '''
    <style>
    .logo-container {
        background: white;
        border-radius: 16px;
        padding: 40px 60px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.12);
        text-align: center;
        border: 3px solid #FFC72C;
        margin: 20px auto;
    }

    .icon-circle {
        width: 50px;
        height: 50px;
        background: #FFC72C;
        border-radius: 50%;
        margin: 0 auto 20px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        box-shadow: 0 4px 16px rgba(255, 199, 44, 0.3);
    }

    .course-code {
        font-size: 20px;
        font-weight: 800;
        color: #FFC72C;
        margin-bottom: 12px;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }

    .main-title {
        font-size: 28px;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 8px;
        line-height: 1.2;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }

    .divider {
        width: 80px;
        height: 3px;
        background: #FFC72C;
        margin: 20px auto;
        border-radius: 2px;
    }

    .subtitle {
        font-size: 16px;
        color: #7f8c8d;
        font-weight: 600;
        font-style: italic;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }
    </style>

    <div class="logo-container">
        <div class="icon-circle">📊</div>
        <div class="course-code">ACCT 605</div>
        <div class="main-title">Data Analytics in Accounting</div>
        <div class="divider"></div>
        <div class="subtitle">Welcome to the interactive practice guide!</div>
    </div>
    '''

def get_how_to_use():
    return '''
However you like! 🤷🏻

But here's my recommendation:

In a typical Snowflake work session, you might find yourself juggling various commands such as 
cloning a database and schema, creating new tables or views, rummaging through files on a stage, keeping tabs on Snowpipe, wrangling data through manual copying, insertion, or updating, etc, etc ... the list is long!

Now, keeping the precise syntax of all these commands at your fingertips, especially for the less-frequently-used ones, can be quite a challenge. 
I recommend keeping this cheat sheet open in a tab while you work. This way, you can swiftly refer to the provided code snippets and easily adapt them to your specific tasks. 
To keep things streamlit 🎈... sorry, I mean streamlined, I have removed options and arguments that are not frequently used in each command. 
However, keep in mind that I have cherry-picked the options based on my personal workflow experience which may not necessarily align with yours.     

Within each segment, there's a special treat ❄️: a bonus section with top tips to elevate your Snowflake skills.  
I suggest that whenever you are using a command for the first time, spend a few minutes reading the tips and hopefully pick up something new.
'''

def get_how_to_use_info():
    return '''
This guide is not intended to be a replacement for the official [Snowflake documentation](https://docs.snowflake.com/) (which is fantastic by the way!). 
    For a comprehensive reference of objects and methods, make sure to explore the official documentation.
'''

def get_how_to_use_feedback():
    return '''
If you happen to spot any errors or have suggestions for improving the descriptions or tips, please don't hesitate to reach out to me directly [here](https://www.linkedin.com/in/siavash-yasini/), or open an [issue](https://github.com/syasini/snowflake_cheatsheet/issues/new) on the GitHub page. Your feedback is invaluable—and relied upon—in keeping this guide accurate and useful.

👈 Don't forget to check the sidebar for additional info and layout options!

Now, go build something awesome on Snowflake! 🚀
'''

def get_excel_text_takeaways():
    return '''
#### **Takeaways**  
- **Flash Fill**:    
  - Automatically extracts first/last names, recombines names into "Last, First" format, and converts to uppercase using Excel's pattern recognition.  
- **Text Formulas**:    
  - `TEXTBEFORE` and `TEXTAFTER` extract first and last names from a full name.  
  - Concatenation (`&`) combines names in the desired format.  
  - `UPPER` converts text to uppercase.  
- **Text to Columns**:    
  - Splits a single column of data (e.g., full names) into multiple columns using delimiters (such as spaces). 
'''

def get_excel_date_takeaways():
    return '''
#### **Takeaways**  
- **Date Formatting**:    
  - Converting date format to "General" reveals Excel’s serial number for the date.  
- `TODAY()` function:    
  - Dynamically enters today’s date.  
- **Date Arithmetic**:    
  - Calculates the number of days between today and regulation release dates.  
- **Extracting Components**:    
  - `YEAR()`, `MONTH()`, and `DAY()` functions dissect dates into their respective parts.  
  - `WEEKDAY()` returns the day of the week as a number; use `VLOOKUP` to display the actual day name (e.g., "Monday").  
'''

def get_excel_pmt_takeaways():
    return '''
#### **Takeaways**  
- **PMT Function**:  
  - Calculates monthly payments for loans based on interest rate, number of periods, and principal amount.  
  - Ideal for analyzing payment sensitivity as interest rates change.  
  - Use **absolute references** to apply the same values across multiple calculations.  
'''

def get_alteryx_overview():
    return '''
#### **Alteryx Overview**

1. **Data Preparation**: Clean and transform data.
2. **Workflow Automation**: Streamline processes.
3. **Collaboration**: Share insights easily.
'''

def get_eu_superstore_overview():
    return '''
#### **EU Superstore Dashboard**

1. **KPIs**: Sales, Profit, Customers.
2. **Map**: Sales by Country.
3. **Line Chart**: Sales by Month.
4. **Bar Chart**: Sales by Product.
'''

def get_libayshuns_overview():
    return '''
#### **Libayshuns Project Overview**

1. **Objective**: Improve customer engagement through personalized marketing.
2. **Data Sources**: CRM, Sales Data, Customer Feedback.
3. **Key Metrics**: Customer Retention, Sales Growth, Campaign ROI.
'''
