import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
#This is defining a variable for over 26
over_26 = df[df['Age'] >= 26]

#THis one is variable for under 26
under_26 = df[df['Age'] < 26]
# This variable, is going to give us our "Unique" parameters, meaning the information in our selected range. 'AGE'
unique_age = df['Age'].unique()
print()
#df is defined as our main rows/columns sheets
print(df)
print("\n People over the age of 26:\n",over_26)
print("\n People under 26:\n",under_26)
print("\nThe Unique Ages are:\n",unique_age)

#This saves the file in a csv format
df.to_csv('output.csv', index=False)