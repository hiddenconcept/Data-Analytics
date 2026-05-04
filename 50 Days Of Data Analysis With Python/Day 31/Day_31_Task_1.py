#In this challenge, you are going to import the employees_record_data dataset, which is a CSV file, and save it to a database.
# #You will then analyze the data using pandas SQL commands. You will use Sqlite3.

#1.Import the employees_record_data dataset and save it as a table in SQL.
#Write code to fetch the table, first using fetchall() and then read_sql_query().

import pandas as pd
import sqlite3 as sql

df = pd.read_csv('employees_record_data.csv')
print("\nEmployee Record Data:\n",df.head())

conn = sql.connect('employees.db')

df.to_sql('employees', conn, if_exists='replace', index=False)

#df read querry
df_results = pd.read_sql_query("SELECT * FROM employees", conn)
print("\nRead Query Data:\n",df_results.head())

#fetchall
cursor = conn.cursor()
cursor.execute("SELECT HireDate FROM employees")
rows = cursor.fetchall()
print("\nFetched Hire Dates:\n")
for row in rows:
    print(row[0])