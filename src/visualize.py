import matplotlib.pyplot as plt

from data_loader import load_transactions_data

# Load prepared dataset
df = load_transactions_data()


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

# To separate the month and year
dm = dm.reset_index()
dm["month"] = dm["month"].dt.to_timestamp()

# Draw a graph
plt.plot(dm["month"], dm["expense"], color="blue", label="Expense")
plt.plot(dm["month"], dm["revenue"], color="red", label="Revenue")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("Revenue & Expense by month")
plt.xticks(rotation=45)
plt.legend()
plt.show()
