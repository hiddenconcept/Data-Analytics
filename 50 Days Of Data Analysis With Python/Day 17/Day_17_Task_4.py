#Creating and modifying DataFrame is an essential skill for data analysts because it allows them to efficiently clean,
#transform, analyze, and report on data. It is a foundational skill that is used in many data-related tasks and workflows.
#In the challenges below, you will create and modify DataFrames.


#Create a DataFrame using the data below:
#sing the .loc attribute, access the age of John from the DataFrame

import pandas as pd
names = ["John","Mary","Peter"]
age= [27,34,47]
sex= ["Male","Female","Female"]

df = pd.DataFrame({"names":names,"age":age,"sex":sex})
print("\nOriginal DataFrame:\n",df)

print("\nJohn's age:\n",df.loc[0,"age"])
