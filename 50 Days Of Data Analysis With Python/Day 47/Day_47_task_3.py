#In this challenge, you are going to work with text data.
# You will import the Text_data CSV file. Here is a sample of the data below:

# 3 Any character that is not a number or in the alphabet is considered a special character.
# Remove special characters from the "text" column.

import pandas as pd

# Import CSV
df = pd.read_csv('text_data.csv')

# Remove special characters from the text column
df['text'] = df['text'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

print(df.head())