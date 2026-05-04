#In this challenge, you are going to import the employees_record_data dataset, which is a CSV file, and save it to a database.
# #You will then analyze the data using pandas SQL commands. You will use Sqlite3.

#2.Using pandas sql_query, what are the names and salaries of employees that make over $60,000.

import pandas as pd
import sqlite3 as sql

df = pd.read_csv('employees_record_data.csv')
print("\nEmployee Record Data:\n",df.head())

conn = sql.connect('employees.db')

df.to_sql('employees', conn, if_exists='replace', index=False)

# Names and salaries of employees earning over $60,000
df_high_earners = pd.read_sql_query(
    "SELECT Name, Salary FROM employees WHERE Salary > 60000",
    conn
)
print("\nEmployees earning over $60,000:\n", df_high_earners)