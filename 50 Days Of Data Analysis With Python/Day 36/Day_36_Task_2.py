#Below, you are going to analyze social media data. You will import the dataset below, which is saved in CSV format.
#The name of the file is social_media.

#2 Which gender has the least number of friends, and what is the total number of friends for this gender?

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

# Group data by gender and calculate total friends
gender_friends = df.groupby("gender")["friends"].sum()

# Find the gender with the least number of friends
least_gender = gender_friends.idxmin()
total_friends = gender_friends.min()

print("\nGender with the least number of friends:")
print(least_gender)

print("\nTotal number of friends for this gender:")
print(total_friends)