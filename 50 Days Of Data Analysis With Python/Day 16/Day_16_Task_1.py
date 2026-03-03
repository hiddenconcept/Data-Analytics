#In the challenges below, you will create and analyze a pandas Series and create a DataFrame from a pandas Series.
#You will use the data below to answer the challenges.
import pandas as pd


list1 = ["wood","red","red","white","blue","red"]

#1. Using pandas, create a pandas Series from the list above.
#Write a code to find how many times each item appears in the list.

series1 = pd.Series(list1)

value_counts = series1.value_counts()

print("\nThe list of items:\n",series1)

print("\nThe List of how many times each item reappears:\n",value_counts)

