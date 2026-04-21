# For the challenges below, you will import and analyze the countries_population_data CSV file.

# 6 Compare the unemployment rates of Switzerland, China, and the USA. Plot a bar plot of this data using Matplotlib.

import warnings
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings('ignore')

# Making pandas show all the tables on the screen
pd.set_option('display.max_columns', None)

# Making pandas show them all in the same line of code
pd.set_option('display.width', None)

df = pd.read_csv('countries_population_data.csv')

# Add Switzerland directly into the DataFrame
df.loc[len(df)] = ['Switzerland', 8654622, 81994, 2.5, 41285]

df_copy = df.copy()

df_sorted = df_copy.sort_values('Population', ascending=False)

print("\n This is the Countries & Population Dataset:\n", df)

# Filter for the 3 countries
unemployment_subset = df[df['Country'].isin(['Switzerland', 'China', 'United States'])]

# Sort by unemployment rate descending
unemployment_subset = unemployment_subset.sort_values('Unemployment_rate', ascending=False)

print("\n Unemployment Rate Comparison:\n", unemployment_subset[['Country', 'Unemployment_rate']])

# Plot
plt.figure(figsize=(8, 6))
bars = plt.bar(unemployment_subset['Country'], unemployment_subset['Unemployment_rate'],
               color=['steelblue', 'tomato', 'seagreen'], edgecolor='black')

# Add value labels on top of each bar
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
             f"{bar.get_height()}%", ha='center', fontsize=11, fontweight='bold')

plt.title('Unemployment Rate Comparison\nSwitzerland vs China vs USA', fontsize=14, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.ylim(0, unemployment_subset['Unemployment_rate'].max() + 1)
plt.tight_layout()
plt.savefig('unemployment_comparison.png', dpi=150)
plt.show()
