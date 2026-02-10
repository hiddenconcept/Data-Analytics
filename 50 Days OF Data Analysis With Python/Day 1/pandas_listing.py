import pandas as pd

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
age = [ "25","30","35","40","45"]
salary = [100000,200000,300000,400000,500000]

pf = pd.DataFrame({"Name":names,"Age":age,"Salary":salary})

print(pf)

