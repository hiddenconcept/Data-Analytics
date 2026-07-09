#In this challenge, you are going to work with text data.
# You will import the Text_data CSV file. Here is a sample of the data below:

# 4 Write a code that adds a column for the length of each row in the text column. Which row has the longest text?

import pandas as pd

# Show full text instead of ...
pd.set_option('display.max_colwidth', None)

# Import CSV
df = pd.read_csv('text_data.csv')

# Remove special characters from the text column
df['text'] = df['text'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

# Add text length column
df['text_length'] = df['text'].str.len()

# Find row with longest text
longest_text = df.loc[df['text_length'].idxmax()]

print("Longest text row:")
print(longest_text)