# This challenge requires that you carry out some cleaning and preprocessing of the data, such as checking for
# duplicates, handling missing values, and manipulating DataFrames.
# You will also be required to provide some insights about the data and much more.

# 5 Using the pandas unstack() method, unstack the DataFrame with a hierarchical index (from question 4).
# The unstacked level should be the two columns: "Player Name" and "Club."
# The "Player Name" column is the outer index. Save this as a new variable.

import pandas as pd

# 1. Import the CSV file
df = pd.read_csv("soccer_strickers.csv")

# Preview the data
print("\nSoccer Strikers:\n", df.head())

# Check column names
print("\nColumn Names:\n", df.columns.tolist())

# Create hierarchical index (from question 4)
df_hierarchical = df.set_index(["Player Name", "Club"])

# 5. Unstack the DataFrame - Club level becomes columns
df_unstacked = df_hierarchical.unstack(level='Club')

print("\nUnstacked DataFrame (Club level moved to columns):")
print(df_unstacked.head(10))

print("\nShape of unstacked DataFrame:", df_unstacked.shape)

print("\nColumn structure (MultiIndex columns):")
print(df_unstacked.columns)

print("\nIndex (Player Name only):")
print(df_unstacked.index[:10])

