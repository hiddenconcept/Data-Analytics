#In this challenge, you are going to work with text data.
# You will import the Text_data CSV file. Here is a sample of the data below:

# 6. For text data to be used in machine learning, it must be
# transformed into numeric vectors. Using Sklearn, tokenize
# the text into numeric vectors.

import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

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

# Create vectorizer
vectorizer = CountVectorizer()

# Convert clean text into numeric vectors
text_vectors = vectorizer.fit_transform(df['clean_text'])

# Convert vectors into DataFrame
vector_df = pd.DataFrame(
    text_vectors.toarray(),
    columns=vectorizer.get_feature_names_out()
)

# Show numeric vectors
print(vector_df.head())

