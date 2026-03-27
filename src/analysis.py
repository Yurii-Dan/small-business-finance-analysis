import pandas as pd

from data_loader import load_transactions_data


# Load prepared dataset
df = load_transactions_data()

# --------------------------------------------------------------------
# BASIC EDA
# --------------------------------------------------------------------

# Display first 5 rows of the dataset
print("\nFirst rows of dataset:")
print(df.head())

# Show dataset structure and column types
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# -------------------------------------------------------------------
# ANALYSIS
# -------------------------------------------------------------------

# Create month, year for aggregation
df["month"] = df["date"].dt.to_period("M")
df["year"] = df["date"].dt.year

# Total revenue, expenses by month
dm = df.pivot_table(
    values="amount",
    index=["year", "month"],
    columns="type",
    aggfunc="sum",
)

# We get rid of NULL
dm["revenue"] = dm["revenue"].fillna(0)
dm["expense"] = dm["expense"].fillna(0)

# Calculate profit
dm["profit"] = dm["revenue"] - dm["expense"]

# Calculate expense, revenue, profit by year
year_total = dm.groupby("year")[["expense", "revenue", "profit"]].sum()
year_total["month"] = "TOTAL"
year_total = year_total.set_index("month", append=True)

# Merge tables
final_df = pd.concat([dm, year_total])
print("\nRevenue, expenses, profit by month and total by year:")
print(final_df)


# Aggregate revenue and expenses by year and category
dc = df.pivot_table(
    values="amount",
    index=["year", "category"],
    columns="type",
    aggfunc="sum",
)

# Replace missing values with 0 for correct calculations
dc["revenue"] = dc["revenue"].fillna(0)
dc["expense"] = dc["expense"].fillna(0)

# Calculate share of expense within each year
dc["expense_%"] = (
    (dc["expense"] / (dc.groupby("year")["expense"].transform("sum"))) * 100
).round(2)

# Calculate share of revenue within each year
dc["revenue_%"] = (
    (dc["revenue"] / (dc.groupby("year")["revenue"].transform("sum"))) * 100
).round(2)

dc = dc.sort_values(by=["year", "expense"], ascending=[True, False])
print("\nCategory analysis (revenue & expenses):")
print(dc)
