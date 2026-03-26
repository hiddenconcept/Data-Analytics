#Count how many times each product appears in the "products" columns. Which product appears the most?

import pandas as pd

# Import JSON file
df = pd.read_json('data.json')

# Count occurrences of each product
product_counts = df['products'].value_counts()
print("Product Counts:\n", product_counts)

# Product that appears the most
most_frequent = df['products'].value_counts().idxmax()
most_frequent_count = df['products'].value_counts().max()
print(f"\nMost Frequent Product: {most_frequent} appearing {most_frequent_count} times")