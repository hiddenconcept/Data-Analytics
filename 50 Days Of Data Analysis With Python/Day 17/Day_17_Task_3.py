#Creating and modifying DataFrame is an essential skill for data analysts because it allows them to efficiently clean,
#transform, analyze, and report on data. It is a foundational skill that is used in many data-related tasks and workflows.
#In the challenges below, you will create and modify DataFrames.


#Write another code using the .at attribute to change the number 9 to 10.

list1 = [[1,2,3],[4,5,6],[7,8,9]]

import pandas as pd
df = pd.DataFrame(list1, columns=["A","B","C"])
print("\nOriginal DataFrame:\n",df)

df.at[2,"C"]= 10

print("\nNew DataFrame:\n",df.at[2,"C"])
