#In this challenge, you are going to work with text data.
# You will import the Text_data CSV file. Here is a sample of the data below:

# 2  Create a copy of the DataFrame and convert the text in the "text" column to lowercase letters.

import pandas as pd

# Import CSV
df = pd.read_csv('text_data.csv')

# Create a copy of the original DataFrame
df_copy = df.copy()

# Convert the 'text' column to lowercase
df_copy['text'] = df_copy['text'].str.lower()

print(df_copy.head())