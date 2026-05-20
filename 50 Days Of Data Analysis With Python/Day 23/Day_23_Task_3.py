#Using the original DataFrame (question 1) with missing values,
# identify and drop any columns that have more than 30% missing values. Save this as a new variable.

import numpy as np
import pandas as pd


names = ["Kelly", np.nan, 'Jon', 'Ken', 'Tim', 'Pel']
grades = [30, 40, 30, 67, np.nan, 55]
age = [15, np.nan, 18, 17, np.nan, 16]

# DataFrame setup
df = pd.DataFrame({'names': names, 'grades': grades, 'age': age})
print("\nDataFrame:\n", df)

# Checking for missing values
print("\nMissing Values Per Column:\n", df.isnull().sum())
print("\nMissing Value Locations (True = missing):\n", df.isnull())

# Make a copy of the original DataFrame
df_filled = df.copy()

# Calculate missing value percentages ---
missing_percent = df.isnull().mean() * 100
print("\nMissing Value Percentage Per Column:\n", missing_percent)


# Identify columns with more than 30% missing values ---
cols_to_drop = missing_percent[missing_percent > 30].index
print("\nColumns to drop (>30% missing):\n", cols_to_drop)


# Drop those columns and save as new variable ---
df_cleaned = df.drop(columns=cols_to_drop)
print("\nCleaned DataFrame (columns with >30% missing dropped):\n",df_cleaned)