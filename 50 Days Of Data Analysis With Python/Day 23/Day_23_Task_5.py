#Use the pandas groupby() method and agg() method to calculate the mean, minimum, and maximum of the "Grades" column,
#grouped by the "Names" column. Use a copy of the DataFrame you saved in question 2.

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

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

# Fill 'names' column with 'Paul' (constant strategy)
name_imputer = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value='Paul')
df_filled['names'] = name_imputer.fit_transform(df_filled[['names']]).ravel()

# Fill 'grades' column with mean strategy
grade_imputer = SimpleImputer(strategy='mean')
df_filled['grades'] = grade_imputer.fit_transform(df_filled[['grades']]).ravel()

# Fill 'age' column with median strategy
age_imputer = SimpleImputer(strategy='median')
df_filled['age'] = age_imputer.fit_transform(df_filled[['age']]).ravel()

print("\n--- After Imputation ---")
print("\nFilled DataFrame:\n", df_filled)
print("\nMissing Values Remaining:\n", df_filled.isnull().sum())
print("\nOriginal DataFrame (unchanged):\n", df)

# ---- NEW: groupby() and agg() on df_filled (copy from question 2) ----
print("\nGrades Grouped by Names\n")
grouped = df_filled.groupby('names')['grades'].agg(
    mean_grade='mean',
    min_grade='min',
    max_grade='max'
)
print(grouped)