import pandas as pd

# 1. Import the CSV file
df = pd.read_csv("soccer_strickers.csv")

# Preview the data
print("\nSoccer Strikers:\n", df.head())

# Check column names
print("\nColumn Names:\n", df.columns.tolist())

# Check data types before cleaning
print("\nData types before cleaning:")
print(df.dtypes)

# Clean the Annual Salary column - remove $, commas, and convert to numeric
df['Annual Salary'] = df['Annual Salary'].str.replace('$', '', regex=False)
df['Annual Salary'] = df['Annual Salary'].str.replace(',', '', regex=False)
df['Annual Salary'] = pd.to_numeric(df['Annual Salary'], errors='coerce')

print("\nData types after cleaning:")
print(df.dtypes)

# Check for any NaN values introduced by conversion
print("\nMissing values in Annual Salary after conversion:", df['Annual Salary'].isnull().sum())

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

# 7. Combined salary of Lionel Messi and Kylian Mbappé
print("\n" + "=" * 80)
print("QUESTION 7: COMBINED SALARY OF LIONEL MESSI AND KYLIAN MBAPPÉ")
print("=" * 80)

try:
    # Get Lionel Messi's annual salary
    messi_salary = df_unstacked.loc["Lionel Messi", "Annual Salary"].sum()
    print(f"\nLionel Messi's total annual salary: ${messi_salary:,.2f}")

    # Get Kylian Mbappé's annual salary
    mbappe_salary = df_unstacked.loc["Kylian Mbappé", "Annual Salary"].sum()
    print(f"Kylian Mbappé's total annual salary: ${mbappe_salary:,.2f}")

    # Calculate combined salary
    combined_salary = messi_salary + mbappe_salary
    print(f"\nCombined annual salary: ${combined_salary:,.2f}")

except KeyError as e:
    print(f"\nError: One or both players not found.")
    print(f"Details: {e}")
    print("\nChecking player names in dataset:")
    print(df_unstacked.index.tolist())