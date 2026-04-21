#For the challenges below, you will import and analyze the countries_population_data CSV file.

#3 Using Matplotlib, create a bar plot to visualize the size of
# the population among the countries. The plot data must be in descending order.

import warnings
import pandas as pd
import matplotlib.pyplot as plt
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

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['Country'], df_sorted['Population'], color='steelblue', edgecolor='black')

plt.title('Population by Country (Descending Order)', fontsize=14, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('population_bar_chart.png', dpi=150)
plt.show()

print("\n Bar chart saved as 'population_bar_chart.png'")