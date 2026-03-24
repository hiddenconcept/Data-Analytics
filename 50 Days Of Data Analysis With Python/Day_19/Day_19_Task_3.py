#Shuffling DataFrames can randomize the data. Write code to reshuffle the index of the DataFrame.

import pandas as pd

names = ["Joe","Phil","Ken","Jos","Luke"]
miles_run = [120,80,100,90,85]
times_in_hrs = [40,38,45,50,50]

df = pd.DataFrame({
    'Name': names,
    'Miles': miles_run,
    'Time in Hours': times_in_hrs,
})

print("\nOriginal DataFrame:\n",df)

a1_names = ["Joe","Phil","Ken","Jos","Luke"]
a1_age = [45,28,21,55,62]
a1_gender = ["Male","Male","Female","Female","Male"]

df_new = pd.DataFrame({
    'Name': a1_names,
    'Age': a1_age,
    'Gender': a1_gender,
})

print("\nNew DataFrame:\n",df_new)

df_combined = pd.concat([df,df_new],ignore_index=True)

print("\nCombined DataFrame:\n",df_combined)

# ✅ Merge side by side on the shared 'Name' column
df_combined_c = pd.merge(df, df_new, on='Name')

print("\nCleaned Up Combined DataFrame:\n",df_combined_c)

df_shuffled = df_combined_c.sample(frac=1).reset_index(drop=True)

print("\nShuffled DataFrame:\n",df_shuffled)