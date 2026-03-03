#In the challenges below, you will create and analyze a pandas Series and create a DataFrame from a pandas Series.
#You will use the data below to answer the challenges.
import pandas as pd


list1 = ["wood","red","red","white","blue","red"]

#2 Using pandas, write code to check if red, white, or black are in the Series.

series1 = pd.Series(list1)

items_to_check = ["red","white","black"]

for item in items_to_check:
    if item in series1:
        print(f"{item} is in the Series")
    else:
        print(f"{item} is not in the Series")
