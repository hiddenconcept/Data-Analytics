#You are given the following data, which is in list format:
# Your task is to analyze and obtain insights from this data using NumPy (do not use pandas).
# Your first task is to create one array from the three (3) lists.
# You will use this array to answer the questions that follow.
import numpy as np

names = ["Kelly","Ben","Jack","Muhammad","Jose","Liz"]
grades = [45,65,75,35,85,40]
classes = ["a","c","e","g","e","f"]

#5.	What is the longest name in the array, and what is its index?

arr = np.array([names,grades,classes])
arr_T = arr.T
print("\nTransposed Array:\n",arr_T)
print()
names_col = arr_T[:, 0]
grades_col = arr_T[:, 1].astype(int)

#Get the length of each name using vectorized approach
name_lengths =np.vectorize(len)(names_col)

#Longest name
longest_index = np.argmax(name_lengths)
longest_name = names_col[longest_index]

print("Longest Name Is:",longest_name)
print("Longest Name Index Is:",longest_index)
print()

#Got the shortest name trying to find the longest, so I thought I would keep it in the code !
#shortest length
shortest_index = np.argmin(name_lengths)
shortest_name = names_col[shortest_index]
print("Shortest Name Is:",shortest_name)
print("Shortest Name Index Is:",shortest_index)





