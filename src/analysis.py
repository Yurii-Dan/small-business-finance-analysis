from data_loader import load_transactions_data

# Load prepared dataset
df = load_transactions_data()

#--------------------------------------------------------------------
# BASIC EDA
#--------------------------------------------------------------------

# Display first 5 rows of the dataset
print("\nFirst rows of dataset:")
print(df.head())

# Show dataset structure and column types
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

#-------------------------------------------------------------------
# ANALYSIS
#-------------------------------------------------------------------
