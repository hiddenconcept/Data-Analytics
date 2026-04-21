#For the challenges below, you will import and analyze the countries_population_data CSV file.

#2 Create a copy of the DataFrame. More information has become available.
# You have a CSV file that has the capital cities. Import the file called countries_data_capital_cities.
#Using the merge() method from pandas, add a capital city column to your DataFrame.

import warnings
import pandas as pd
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

print("\n This is the Countries & Population Dataset:\n",df)
print("\n This is the Merged Dataset:\n",df_copy)