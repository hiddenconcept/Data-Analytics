#In the challenges below, you will create and analyze a pandas Series and create a DataFrame from a pandas Series.
#You will use the data below to answer the challenges.
import pandas as pd


list1 = ["wood","red","red","white","blue","red"]

# Using pandas, write code to return all unique values from the Series.

series1 = pd.Series(list1)

unique_values = series1.unique()
print("\nUnique values in the series:\n",unique_values)
