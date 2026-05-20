#Create a pandas DataFrame from the lists above.
# Write a code to check if there are any missing values in the columns of the DataFrame.
import numpy as np
import pandas as pd

names = ["Kelly", np.nan, 'Jon', 'Ken', 'Tim','Pel']
grades = [30,40,30,67, np.nan, 55]
age = [15, np.nan,18,17, np.nan, 16]


#DataFrame setup
df = pd.DataFrame({'names': names, 'grades': grades, 'age': age})
print("\nDataFrame:\n",df)

#Checking for missing values
print("\nMissing Values Per Column:\n",df.isnull().sum())


print("\nMissing Value Locations(True = missing):\n",df.isnull())
