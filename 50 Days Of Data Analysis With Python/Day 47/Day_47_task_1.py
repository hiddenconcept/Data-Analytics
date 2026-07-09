#In this challenge, you are going to work with text data.
# You will import the Text_data CSV file. Here is a sample of the data below:

#1  Import the Text_data dataset. Write a code that checks if there are duplicates in the "text" column.

import pandas as pd

# Import CSV
df = pd.read_csv('text_data.csv')

print(df.head())
print()
# Check for duplicates in the 'text' column
duplicate_count = df['text'].duplicated().sum()
print(f"Number of duplicate entries in 'text' column: {duplicate_count}")

# Optional: view the actual duplicate rows
duplicates = df[df['text'].duplicated(keep=False)]
print(duplicates)