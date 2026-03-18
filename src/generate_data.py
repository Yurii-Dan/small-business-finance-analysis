import random
from datetime import datetime, timedelta
import csv
import os

# Define date range
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

current_date = start_date

# Categories for random transactions
expense_categories = ["marketing", "utilities", "software"]
revenue_categories = ["sales", "services"]

# Amount ranges for each category
expense_ranges = {    
    "marketing": (500, 3000),
    "utilities": (300, 1500),
    "software": (100, 1000)
}

revenue_ranges = {
    "sales": (2000, 10000),
    "services": (1000, 5000)
}

# List to store generated transactions
transactions = []

# Main loop through each day
while current_date <= end_date:
    
    # Convert date to string format
    date_str = current_date.strftime("%Y-%m-%d")

    # Fixed monthly rent (1st day of month)
    if current_date.day == 1:
        transactions.append([date_str, "expense", "rent", 8000])

    # Monthly salary (25th day, variable amount)
    if current_date.day == 25:
        amount = random.randint(10000, 20000)
        transactions.append([date_str, "expense", "salary", amount])

    # Random number of transactions per day
    transactions_per_day = random.randint(0, 3)

    for _ in range(transactions_per_day):

        # Choose transaction type with probability
        transaction_type = random.choices(
            ["expense", "revenue"],
            weights=[0.4, 0.6]
        )[0]

        if transaction_type == "expense":
            category = random.choice(expense_categories)
            amount = random.randint(*expense_ranges[category])
        else:
            category = random.choices(
                revenue_categories,
                weights=[0.7, 0.3]
            )[0]
            amount = random.randint(*revenue_ranges[category])

        # Append transaction
        transactions.append([date_str, transaction_type, category, amount])

    # Move to next day
    current_date += timedelta(days=1)

# Build correct path to /data folder
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
file_path = os.path.join(base_path, "data", "transactions.csv")

# Save to CSV file
with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["date", "type", "category", "amount"])

    # Write data
    writer.writerows(transactions)