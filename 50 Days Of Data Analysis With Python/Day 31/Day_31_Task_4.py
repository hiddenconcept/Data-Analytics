#In this challenge, you are going to import the employees_record_data dataset, which is a CSV file, and save it to a database.
# #You will then analyze the data using pandas SQL commands. You will use Sqlite3.

#4 Which department has the highest-paid employee?
# What is their name?

import pandas as pd
import sqlite3 as sql

df = pd.read_csv('employees_record_data.csv')
print("\nEmployee Record Data:\n",df.head())

conn = sql.connect('employees.db')

df.to_sql('employees', conn, if_exists='replace', index=False)

# Department and name of the highest-paid employee
df_top = pd.read_sql_query(
    "SELECT Name, Department, Salary FROM employees ORDER BY Salary DESC LIMIT 1",
    conn
)
print("\nHighest-Paid Employee:\n", df_top)