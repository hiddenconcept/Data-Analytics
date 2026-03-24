import pandas as pd

df = pd.read_csv('asset_data_analysis.csv')
df.to_json('data.json', orient='records', indent=2)

print("Your conversion is complete.")