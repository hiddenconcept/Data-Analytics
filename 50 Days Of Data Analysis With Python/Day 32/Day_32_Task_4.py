# This challenge requires that you carry out some cleaning and preprocessing of the data, such as checking for
# duplicates, handling missing values, and manipulating DataFrames.
# You will also be required to provide some insights about the data and much more.

# 4  Create a hierarchical index for your DataFrame. Set the "Player Name" and the "Club" as index columns.
# Using th.loc attribute, filter the DataFrame to find the annual salary of Romelu Lukaku.

import pandas as pd

# 1. Import the CSV file
df = pd.read_csv("soccer_strickers.csv")

# Preview the data
print("\nSoccer Strikers:\n", df.head())

# Check column names
print("\nColumn Names:\n", df.columns.tolist())

# Check for duplicates before creating hierarchical index
print("\nDuplicate rows:", df.duplicated().sum())

# Check for missing values in key columns
print("\nMissing values:\n", df[["Player Name", "Club", "Annual Salary"]].isnull().sum())

# 4. Create hierarchical index
df_hierarchical = df.set_index(["Player Name", "Club"])
print("\nHierarchical Index created successfully!")
print("\nDataFrame with hierarchical index:\n", df_hierarchical.head())

# Filter for Romelu Lukaku's annual salary using .loc
try:
    # This will handle cases where Lukaku might play for multiple clubs
    lukaku_salary = df_hierarchical.loc["Romelu Lukaku"]

    if isinstance(lukaku_salary, pd.Series):
        # Single club - Series returned
        print(f"\nRomelu Lukaku's Annual Salary: {lukaku_salary['Annual Salary']}")
        print(f"Club: {lukaku_salary.name}")  # The club is the remaining index
    else:
        # Multiple clubs - DataFrame returned
        print(f"\nRomelu Lukaku's Annual Salary across clubs:\n{lukaku_salary['Annual Salary']}")

except KeyError:
    print("\nRomelu Lukaku is not in the dataset.")

    # Show available players for reference
    print("\nAvailable players:")
    print(df_hierarchical.index.get_level_values(0).unique()[:10])
