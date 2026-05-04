#In this challenge, you are going to import the employees_record_data dataset, which is a CSV file, and save it to a database.
# #You will then analyze the data using pandas SQL commands. You will use Sqlite3.

#3  Write code to return the average salary for each department. Group it by department.

import pandas as pd
import sqlite3 as sql

df = pd.read_csv('employees_record_data.csv')
print("\nEmployee Record Data:\n",df.head())

conn = sql.connect('employees.db')

df.to_sql('employees', conn, if_exists='replace', index=False)

# Average salary grouped by department
df_avg_salary = pd.read_sql_query(
    "SELECT Department, AVG(Salary) AS AvgSalary FROM employees GROUP BY Department",
    conn
)
print("\nAverage Salary by Department:\n", df_avg_salary)