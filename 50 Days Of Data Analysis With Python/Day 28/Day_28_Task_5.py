#For the challenges below, you will import and analyze the countries_population_data CSV file.

#5 Using pandas, return a subset of the top three countries with the lowest GDP. Assign this to a variable.

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

# Get the top 3 countries with the lowest GDP per capita
lowest_gdp = df_copy.nsmallest(3, 'GDP_per_capita')

# Plot the top 3 countries with the lowest GDP per capita
plt.figure(figsize=(10, 6))
plt.bar(lowest_gdp['Country'], lowest_gdp['GDP_per_capita'], color='tomato', edgecolor='black')

plt.title('Top 3 Countries with the Lowest GDP per Capita', fontsize=14, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('GDP per Capita (USD)', fontsize=12)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()



print("\n Top 3 Countries with the Lowest GDP per Capita:\n", lowest_gdp)