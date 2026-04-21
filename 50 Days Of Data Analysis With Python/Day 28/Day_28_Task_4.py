#For the challenges below, you will import and analyze the countries_population_data CSV file.

#4 Using NumPy, calculate the correlation between the population and GDP per capita for each country and create
#a scatter plot to visualize the relationship between the two variables (population and GDP per capita) using Matplotlib.

import warnings
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
warnings.filterwarnings('ignore')

#Making pandas show all the tables on the screen
pd.set_option('display.max_columns', None)

#Making pandas show them all in the same line of code
pd.set_option('display.width', None)

df = pd.read_csv('countries_population_data.csv')

df_copy = df.copy()

#Import Capital Cities CSV
df_capitals = pd.read_csv('countries_data_capital_cities.csv')

#Merge the 2 tables
df_copy = pd.merge(df_copy,df_capitals,how='left',on='Country')

df_sorted = df_copy.sort_values('Population',ascending=False)

print("\n This is the Countries & Population Dataset:\n",df)
print("\n This is the Merged Dataset:\n",df_copy)

# Calculate correlation using NumPy
correlation = np.corrcoef(df_copy['Population'], df_copy['GDP_per_capita'])[0, 1]
print(f"\n Correlation between Population and GDP per Capita: {correlation:.4f}")

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_copy['Population'], df_copy['GDP_per_capita'], color='steelblue', edgecolor='black', s=100)

# Label each point with the country name
for i, row in df_copy.iterrows():
    plt.text(row['Population'], row['GDP_per_capita'], f"  {row['Country']}", fontsize=9, va='center')

plt.title(f'Population vs GDP per Capita\n(Correlation: {correlation:.4f})', fontsize=14, fontweight='bold')
plt.xlabel('Population', fontsize=12)
plt.ylabel('GDP per Capita (USD)', fontsize=12)
plt.tight_layout()
plt.savefig('population_vs_gdp_scatter.png', dpi=150)
plt.show()

print("\n Scatter plot saved as 'population_vs_gdp_scatter.png'")