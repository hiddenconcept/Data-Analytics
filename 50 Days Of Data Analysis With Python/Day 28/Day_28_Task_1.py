#For the challenges below, you will import and analyze the countries_population_data CSV file.

#1 Using pandas, import the CSV file of the country's data.
#Import the warnings module and use it to "ignore" the warnings.

import warnings
import pandas as pd
warnings.filterwarnings('ignore')

df = pd.read_csv('countries_population_data.csv')

print("\n This is the Countries & Population Dataset:\n",df)