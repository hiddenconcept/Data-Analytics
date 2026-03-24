# Create a DataFrame from the lists above using pandas

import pandas as pd

names = ["Joe","Phil","Ken","Jos","Luke"]
miles_run = [120,80,100,90,85]
times_in_hrs = [40,38,45,50,50]

df = pd.DataFrame({
    'Name': names,
    'Miles': miles_run,
    'Time in Hours': times_in_hrs,
})

print(df)
