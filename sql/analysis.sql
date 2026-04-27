-- Create transactions table
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    date DATE,
    type TEXT,
    category TEXT,
    amount NUMERIC
);

-- ========================================
-- BASIC EDA 
-- ========================================

-- Display first 10 rows of the dataset
SELECT * FROM transactions LIMIT 10;

-- Print the number of rows in the table
SELECT COUNT(*) FROM transactions;

-- Check for missing values
SELECT *
FROM transactions
WHERE date IS NULL OR type IS NULL OR category IS NULL OR amount IS NULL;

-- Check unique categories
SELECT DISTINCT category FROM transactions;

-- ========================================
-- BASIC KPI (Simple approach)
-- ========================================

-- Calculate total revenue, expenses, profit (KPI)
SELECT 
    SUM(CASE WHEN type = 'revenue' THEN amount ELSE 0 END) AS total_revenue,
    SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_expenses,
    SUM(CASE WHEN type = 'revenue' THEN amount ELSE 0 END) 
    - SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_profit
FROM transactions;

-- ========================================
-- KPI (CTE version - cleaner approach)
-- ========================================

-- NOTE:
-- This query calculates KPIs for the entire dataset.
-- To limit analysis to a specific period, add a date filter in each CTE:
-- Example:
-- WHERE date BETWEEN '2025-01-01' AND '2025-12-31'

WITH total_revenue AS (
	SELECT
		SUM(amount) AS total_revenue
	FROM transactions
	WHERE type = 'revenue'
	 -- AND date BETWEEN '2025-01-01' AND '2025-12-31'
),
total_expenses AS(
	SELECT
		SUM(amount) AS total_expenses
	FROM transactions
	WHERE type = 'expense'
	 -- AND date BETWEEN '2025-01-01' AND '2025-12-31'
	)
SELECT
	tr.total_revenue,
	te.total_expenses,
	tr.total_revenue - te.total_expenses AS total_profit
FROM total_revenue tr
CROSS JOIN total_expenses te;

-- ========================================
-- MONTHLY ANALYSIS (Simple approach)
-- ========================================

-- Total revenue, expenses by month
SELECT
	DATE_TRUNC('month', t.date)::date AS month,
	SUM(CASE WHEN type = 'revenue' THEN amount ELSE 0 END) AS revenue,
	SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS expenses,
	SUM(CASE WHEN type = 'revenue' THEN amount ELSE 0 END) 
    - SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS profit
FROM transactions t	
GROUP BY month
ORDER BY month;

-- ========================================
-- MONTHLY ANALYSIS (CTE version )
-- ========================================

WITH prepared_data AS (
    SELECT
        DATE_TRUNC('month', t.date)::date AS month,
        CASE WHEN type = 'revenue' THEN amount ELSE 0 END AS revenue_part,
		CASE WHEN type = 'expense' THEN amount ELSE 0 END AS expense_part
	FROM transactions t	
)
SELECT
    month,
    SUM(revenue_part) AS revenue,
    SUM(expense_part) AS expenses,
	SUM(revenue_part) - SUM(expense_part) AS profit
FROM prepared_data
GROUP BY month
ORDER BY month;

-- ========================================
-- Top expense categories
-- ========================================

-- Calculates:
-- 1. Total expenses by category
-- 2. Ranking of categories by expenses
-- 3. Contribution (%) of each category
-- 4. Cumulative percentage (Pareto 80/20 analysis)

WITH category_expenses AS (
    SELECT
        category,
        SUM(amount) AS total_expenses
    FROM transactions
    WHERE type = 'expense'
	-- AND date BETWEEN '2025-01-01' AND '2025-12-31'
    GROUP BY category
)
SELECT
    category,
    total_expenses,
    RANK() OVER (ORDER BY total_expenses DESC) AS expense_rank,
	ROUND(100.0 * total_expenses / SUM(total_expenses) OVER (), 2) AS contribution_percent,
	ROUND(
    100.0 * SUM(total_expenses) OVER (ORDER BY total_expenses DESC)
    / SUM(total_expenses) OVER (),
    2
) AS cumulative_percent
FROM category_expenses
ORDER BY total_expenses DESC;
