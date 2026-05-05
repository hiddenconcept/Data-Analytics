# This challenge requires that you carry out some cleaning and preprocessing of the data, such as checking for
# duplicates, handling missing values, and manipulating DataFrames.
# You will also be required to provide some insights about the data and much more.

# 1 Import the soccer_strickers CSV file using pandas. Check for  missing data, duplicates and column data types.
# If any duplicates, drop them.

import pandas as pd

# 1. Import the CSV file
df = pd.read_csv("soccer_strickers.csv")

# Preview the data
print("\nSoccer Strikers:\n", df.head())

# Check column data types
print("\nChecking Data Types:\n", df.dtypes)

# Check for missing data
print("\nMissing Values Per Column:\n", df.isnull().sum())
print(f"Total Missing Values: {df.isnull().sum().sum()}")

# Check for and drop duplicates
duplicate_count = df.duplicated().sum()
print(f"\nChecking for Duplicates: {duplicate_count}")

if duplicate_count > 0:
    df = df.drop_duplicates()
    print(f"✓ Duplicates dropped. Updated shape: {df.shape}")
else:
    print("✓ No duplicates found.")

# General summary
print("\nDataset Info:")
df.info()

