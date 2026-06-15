#In this challenge, you will analyze and transform data.
# You will import the cars_and_careers CSV file. Here is a sample of the dataset below:

#6 Which car is driven by the oldest person?
# Using Matplotlib, plot a bar plot of the cars driven by the 5 oldest people and their ages in descending order.

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('cars_and_careers.csv')

# Shift rows down by 1
df = df.shift(1)

# Insert new row at index 0
df.iloc[0] = ["Casy", "Unknown", 31, "Ford"]

# Remove last row
df = df.iloc[:-1]

# Convert Age column to numeric
df['Age'] = pd.to_numeric(df['Age'])

# Sort by age (descending)
df_sorted = df.sort_values(by='Age', ascending=False)

# Oldest person
oldest = df_sorted.iloc[0]

print("Oldest Person:")
print("Name:", oldest['Name'])
print("Age:", oldest['Age'])
print("Car:", oldest['Car'])

# Top 5 oldest people
top5 = df_sorted.head(5)

# Bar plot
plt.figure(figsize=(8, 5))
plt.bar(top5['Car'], top5['Age'])
plt.title('Cars Driven by the 5 Oldest People')
plt.xlabel('Car')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()