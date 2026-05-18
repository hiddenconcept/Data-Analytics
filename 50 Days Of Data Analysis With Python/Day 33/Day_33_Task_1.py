# 1 Using pandas, import the website_data_analysis dataset and find the average number of visits per website.
import pandas as pd

# Load the dataset
df = pd.read_csv("website_data_analysis.csv")

# Find the average number of visits per website
average_visits = df.groupby("website")["visits"].mean()

# Display the result
print(average_visits)