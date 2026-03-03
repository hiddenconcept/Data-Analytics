#In the challenges below, you will create and analyze a pandas Series and create a DataFrame from a pandas Series.
#You will use the data below to answer the challenges.
import pandas as pd

list1 = ["wood","red","red","white","blue","red"]
#4. Write code to check the number of dimensions of your updated Series (question 4).
# Write another line of code to convert the Series into a DataFrame.  Your DataFrame should have one column of colors.
# Check the shape and number of dimensions of your DataFrame.
# Your dataframe must have a shape of (6,1)

series1 = pd.Series(list1)
print("\nOriginal Series:\n",series1)

updates = pd.Series({0:"green",2:"orange"})
series1.update(updates)
print("\nSeries updated:\n",series1)
print("\nNumber of Dimensions:\n",series1.ndim)

#Going by colours as per the question objective
df = series1.to_frame(name="color")
print("\nOriginal DataFrame:\n",df)

#Checking shape and dimensions
print("\nDataFrame Shape:\n",df.shape)
print("\nDataframe Dimensions:\n",df.ndim)