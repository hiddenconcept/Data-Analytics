# This challenge requires that you carry out some cleaning and preprocessing of the data, such as checking for
# duplicates, handling missing values, and manipulating DataFrames.
# You will also be required to provide some insights about the data and much more.

# 3 Which player has the highest goal conversion rate (goals scored as a percentage of chances created)?

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

df_copy = df.copy()

print("\nBefore Conversion:")
print(df_copy["Annual Salary"].dtype)
print(df_copy["Annual Salary"].head())

# Strip currency symbols and commas, then convert to float (FIXED VERSION)
df_copy["Annual Salary"] = (
    df_copy["Annual Salary"]
    .str.replace(r"[$,]", "", regex=True)  # Remove only $ and commas, keep decimal
    .astype(float)
)

print("\nAfter Conversion:")
print(df_copy["Annual Salary"].dtype)
print(df_copy["Annual Salary"].head())

# Handle missing values in critical columns
print(f"\nRows before handling missing values: {len(df_copy)}")
df_copy = df_copy.dropna(subset=["Goals", "Chances Created", "Player Name"])
print(f"Rows after handling missing values: {len(df_copy)}")

# Calculate Goal Conversion Rate (with zero-division handling)
df_copy["Goal Conversion Rate"] = df_copy.apply(
    lambda row: (row["Goals"] / row["Chances Created"] * 100)
    if row["Chances Created"] > 0 else 0,
    axis=1
)

# Check for data quality issues
invalid_rows = df_copy[df_copy["Goals"] > df_copy["Chances Created"]]
if len(invalid_rows) > 0:
    print(f"\n⚠️ Warning: {len(invalid_rows)} players have more goals than chances created")
    print(invalid_rows[["Player Name", "Goals", "Chances Created"]])

# Find the player with the highest conversion rate
top_player = df_copy.loc[df_copy["Goal Conversion Rate"].idxmax()]

# Display results
print("\nPlayer With Highest Goal Conversion Rate:\n")
print(f"Player: {top_player['Player Name']}")
print(f"Goal Conversion Rate: {top_player['Goal Conversion Rate']:.2f}%")
print(f"Goals: {int(top_player['Goals'])}")
print(f"Chances Created: {int(top_player['Chances Created'])}")