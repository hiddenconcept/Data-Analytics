#Below, you are going to analyze social media data. You will import the dataset below, which is saved in CSV format.
#The name of the file is social_media.

#1 Load the data using pandas. Which location has the most active users based on total posts?
# What is the total number of posts in this location?

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