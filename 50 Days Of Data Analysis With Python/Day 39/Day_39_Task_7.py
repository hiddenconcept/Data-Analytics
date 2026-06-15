#In this challenge, you will analyze and transform data.
# You will import the cars_and_careers CSV file. Here is a sample of the dataset below:

#7 or data to be used in machine learning algorithms, it must be converted to a numerical format.
# This is because machine learning algorithms can only understand numbers.
#Your task now is to write code that will convert the text columns into numeric data types for machine
# learning using first, pandas and then Sklearn.
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv('cars_and_careers.csv')

# Shift rows down by 1
df = df.shift(1)

# Insert new row at index 0
df.iloc[0] = ["Casy", "Unknown", 31, "Ford"]

# Remove last row
df = df.iloc[:-1]


# Pandas Encoding

df_pandas = df.copy()

for col in ['Name', 'Occupation', 'Car']:
    df_pandas[col] = df_pandas[col].astype('category').cat.codes

print("Pandas Encoded Data:")
print(df_pandas.head())


# Scikit-Learn Encoding

df_sklearn = df.copy()

for col in ['Name', 'Occupation', 'Car']:
    encoder = LabelEncoder()
    df_sklearn[col] = encoder.fit_transform(df_sklearn[col])

print("\nScikit-Learn Encoded Data:")
print(df_sklearn.head())