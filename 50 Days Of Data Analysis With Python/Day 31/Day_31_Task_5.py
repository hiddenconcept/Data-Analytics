#In this challenge, you are going to import the employees_record_data dataset, which is a CSV file, and save it to a database.
# #You will then analyze the data using pandas SQL commands. You will use Sqlite3.

#5 Which employees were hired before 2020-01-01?

import pandas as pd
import sqlite3 as sql

df = pd.read_csv('employees_record_data.csv')
print("\nEmployee Record Data:\n",df.head())

conn = sql.connect('employees.db')

df.to_sql('employees', conn, if_exists='replace', index=False)

# Fetch all employees then filter by HireDate in pandas
df_all = pd.read_sql_query("SELECT Name, HireDate FROM employees", conn)

# Convert HireDate to datetime so comparisons work correctly
df_all['HireDate'] = pd.to_datetime(df_all['HireDate'], format='%d %m %Y')

# Filter for hired before 2020
df_before_2020 = df_all[df_all['HireDate'] < '2020-01-01']
print("\nEmployees hired before 2020:\n", df_before_2020)