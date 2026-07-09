#In this challenge, you are going to work with text data.
# You will import the Text_data CSV file. Here is a sample of the data below:

# 6 Stopwords are common words that are typically removed from text data before performing natural language processing tasks,
# such as text classification, sentiment analysis, or information retrieval.
# Examples of stop words include "the," "and," "a," "an," "in," "of," "to," etc.
# Write code to remove stop words from the text using the nltk module.

import pandas as pd
import nltk
from nltk.corpus import stopwords

# Download stopwords (only needed once)
nltk.download('stopwords')

# Import CSV
df = pd.read_csv('text_data.csv')

# Remove missing values
df['text'] = df['text'].fillna('')

# Remove special characters
df['text'] = df['text'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

# Create stopword list
stop_words = set(stopwords.words('english'))

# Remove stopwords
df['clean_text'] = df['text'].apply(
    lambda x: ' '.join(
        word for word in x.split()
        if word.lower() not in stop_words
    )
)

# Show results
print(df[['text', 'clean_text']].head())