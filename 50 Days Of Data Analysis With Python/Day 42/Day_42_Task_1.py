#For this challenge, you are going to preprocess, analyze, and create visualizations of the toys_sales_data dataset.
#Here is a snippet of the dataset below:

#1 Load the CSV file using pandas.
# Check the data types of the "Date" and "Total Sales" columns.

import pandas as pd

df = pd.read_csv('toys_sales_data.csv')

print("\nToy Sales dataset:\n",df.head())

print("\nToy Sales Datatypes:\n",df.dtypes)