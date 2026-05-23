#Below, you are going to analyze social media data. You will import the dataset below, which is saved in CSV format.
#The name of the file is social_media.

#3 What is the gender, location, and age of the most active user based on posts?

import pandas as pd
import numpy as np


df = pd.read_csv("social_media.csv")

# Group data by location and calculate total posts
location_posts = df.groupby("location")["posts"].sum()

# Find the location with the highest number of posts
top_location = location_posts.idxmax()
total_posts = location_posts.max()

print("\nLocation with the most active users:")
print(top_location)

print("\nTotal number of posts in this location:")
print(total_posts)

# Find the row with the highest number of posts
most_active_user = df.loc[df["posts"].idxmax()]

# Display gender, location, and age
print("\nMost Active User Information:")
print("Gender:", most_active_user["gender"])
print("Location:", most_active_user["location"])
print("Age:", most_active_user["age"])

