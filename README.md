# Financial Data Analysis Project

This project simulates and analyzes financial data for a small business to uncover trends, identify key cost drivers, and highlight opportunities for optimization.

The analysis is performed using Python (Pandas, Matplotlib), with plans to extend the project using SQL and Tableau for advanced analytics and visualization.

## Dataset Description
The dataset contains daily financial transactions for the year 2025, including:
- Revenue (Sales, Services)
- Expenses (Salary, Marketing, Operations, etc.)
- Transaction date

## Tools & Technologies
- Python (Pandas, Matplotlib)
- CSV-based data storage
- Tableau

## Project Structure
- data/ — dataset
- src/ — source code
- outputs/ — generated visualizations

## How to Use

This project can be adapted for analyzing financial data of any small business.

To use it with your own data:
1. Replace the `transactions.csv` file with your dataset
2. Ensure the following structure is preserved:
   - `date` — transaction date
   - `type` — revenue or expense
   - `category` — category of transaction
   - `amount` — transaction value

The analysis scripts and visualizations will automatically adapt to the new data. This makes the project reusable for real-world business scenarios.

## Visualizations

![Revenue & Expense](outputs/revenue_expense.png)
![Profit](outputs/profit.png)

## Tableau Dashboard

![Dashboard Overview](outputs/dashboard_overview.png)

### KPI Overview

![KPI Overview](outputs/kpi.png)

### Trend Analysis

![Trend Analysis](outputs/trend.png)

### Expense Breakdown

![Expense Breakdown](outputs/breakdown.png)

The interactive dashboard was built in Tableau to complement the Python analysis and provide a business-oriented view of financial performance.

**Key features:**

* KPI tracking: Revenue, Expenses, Profit, Profit Margin
* Time-series analysis of revenue and profit trends
* Expense breakdown by category
* Dynamic Top N filtering using a parameter
* Interactive filtering for flexible data exploration

**File:**

* `outputs/finance_dashboard.twbx`

## SQL Analysis (PostgreSQL)

This project includes SQL-based data analysis using PostgreSQL.

### Key components:

* **Exploratory Data Analysis (EDA)**
  Basic dataset validation and structure checks

* **KPI Calculation**
  Total revenue, expenses, and profit (simple and CTE-based approaches)

* **Time-based Analysis**
  Monthly aggregation of financial metrics

* **Category Analysis**
  Expense breakdown by category

* **Advanced SQL (Window Functions)**

  * Ranking categories by expenses
  * Contribution (%) calculation
  * Cumulative percentage (Pareto analysis)

All queries are available in the `sql/analysis.sql` file.


## Key Insights
Insights are derived from Python analysis, SQL queries, and the Tableau dashboard.

### Financial Overview
- The business is profitable throughout the year
- Total annual profit: 1,012,298
- Average profit margin: ~65%
- Profitability shows clear seasonal variation
- Total annual revenue and expenses are clearly visualized through KPI tracking in the dashboard

### Revenue Trends
- Revenue peaks in January, followed by a decline in February–March
- Secondary growth in August–September
- Clear seasonality pattern confirmed by both time-series analysis and dashboard visualization

### Expense Analysis
- Salary (~35%) and Marketing (~28%) are the largest cost drivers
- Fixed costs exceed 50% of total expenses
- Marketing is the most flexible cost for optimization

### Revenue Structure
- Sales: ~80%
- Services: ~20%
- The business shows high dependency on a single revenue stream

### Business Implications
- There is a need for customer retention strategies after the peak season
- Opportunity to optimize marketing efficiency
- Potential to diversify revenue sources
- Interactive filtering allows dynamic exploration of high-cost categories
- Top N analysis highlights the most impactful expense drivers

## Future Improvements
- Implement forecasting for revenue and profit
