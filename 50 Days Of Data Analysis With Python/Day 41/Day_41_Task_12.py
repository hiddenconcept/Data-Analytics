#In this challenge, you are going to gain insights and preprocess fictitious population data.
#You will import the population_data file, which is saved in CSV format.

# 12 Using Matplotlib, plot a histogram of the population in the dataset.
# The number of bins for your plot must be 10.
# Your plot must have axis labels and a title.
# Your plot title's font size must be 20. Make your title bold.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Import population dataset
df = pd.read_csv('population_data.csv')

# Check missing values
missing_values = df.isnull().sum()

print("\nMissing Values by Column:\n", missing_values)

# Count unique countries
unique_countries = df['Country'].nunique()

print("\nNumber of Unique Countries:", unique_countries)

# Find country with the smallest urban population
smallest_urban_country = df.loc[df['Urban Population'].idxmin(), 'Country']
smallest_urban_population = df['Urban Population'].min()

print("\nCountry with the Smallest Urban Population:", smallest_urban_country)
print("Urban Population:", smallest_urban_population)

# Create histogram of Population
plt.figure(figsize=(10, 6))

plt.hist(df['Population'], bins=10)

# Add axis labels
plt.xlabel("Population")
plt.ylabel("Frequency")

# Add title
plt.title("Distribution of Population Across Countries",
          fontsize=20,
          fontweight='bold')

# Format population numbers
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

# Show plot
plt.show()