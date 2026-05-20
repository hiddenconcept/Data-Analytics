#Your supervisor has asked that you show them how to fill in the missing values using the library's Sklearn.
# Write code to fill in missing values in the DataFrame above using this library.
#Replace the missing value in the "Name" column with the name "Paul."
# Use the mean strategy for the "Grades" column and the median strategy for the "Age" column.
#Make a copy of the original DataFrame.

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
df_filled['names'] = name_imputer.fit_transform(df_filled[['names']]).ravel()  # ✅ 'names' + double brackets

# Fill 'grades' column with mean strategy
grade_imputer = SimpleImputer(strategy='mean')
df_filled['grades'] = grade_imputer.fit_transform(df_filled[['grades']]).ravel()  # ✅ 'grades' + double brackets

# Fill 'age' column with median strategy
age_imputer = SimpleImputer(strategy='median')
df_filled['age'] = age_imputer.fit_transform(df_filled[['age']]).ravel()  # ✅ double brackets

print("\n--- After Imputation ---")
print("\nFilled DataFrame:\n", df_filled)
print("\nMissing Values Remaining:\n", df_filled.isnull().sum())
print("\nOriginal DataFrame (unchanged):\n", df)