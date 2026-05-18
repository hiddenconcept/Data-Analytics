# This challenge requires that you carry out some cleaning and preprocessing of the data, such as checking for
# duplicates, handling missing values, and manipulating DataFrames.
# You will also be required to provide some insights about the data and much more.

# 6 How many chances were created by Karim Benzema? Use the unstack DataFrame from question 5.

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

# 6. Find chances created by Karim Benzema
try:
    # Access the 'Chances Created' row for Karim Benzema
    benzema_chances = df_unstacked.loc["Karim Benzema", "Chances Created"]

    print("\n" + "=" * 80)
    print("QUESTION 6: CHANCES CREATED BY KARIM BENZEMA")
    print("=" * 80)
    print("\nChances created by Karim Benzema:")
    print(benzema_chances)

    # Sum across all clubs (in case he played for multiple clubs)
    total_chances = benzema_chances.sum()
    print(f"\nTotal chances created: {total_chances}")

except KeyError:
    print("\nKarim Benzema is not in the dataset or 'Chances Created' column doesn't exist.")
    print("\nAvailable players:")
    print(df_unstacked.index[:10])
