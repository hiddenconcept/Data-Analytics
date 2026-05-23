#Below, you are going to analyze social media data. You will import the dataset below, which is saved in CSV format.
#The name of the file is social_media.

#5 Using a pie plot type, compare the number of male and female users.
# Present your answer in percentages. Use only Matplotlib.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("social_media.csv")

# Create a subset with only female users
female_users = df[df["gender"] == "female"]

# Count female users by city
female_city_counts = female_users["location"].value_counts()

# Find the city with the highest number of female users
top_female_city = female_city_counts.idxmax()
female_count = female_city_counts.max()

print("\nCity with the highest number of female users:")
print(top_female_city)

print("\nNumber of female users in this city:")
print(female_count)

# Count male and female users
gender_counts = df["gender"].value_counts()

# Create pie chart
plt.figure(figsize=(6, 6))

plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Percentage of Male and Female Users")

# Display the plot
plt.show()