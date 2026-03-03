#In the challenges below, you will create and analyze a pandas Series and create a DataFrame from a pandas Series.
#You will use the data below to answer the challenges.
import pandas as pd

list1 = ["wood","red","red","white","blue","red"]
#4. Using the pandas update() method, write code to update the Series you created in question 1.
# Add green and orange to the series. The color green will be at index 0, and orange will be at index 2.
series1 = pd.Series(list1)
print("\nOriginal Series:\n",series1)

updates = pd.Series({0:"green",2:"orange"})
series1.update(updates)
print("\nSeries updated:\n",series1)