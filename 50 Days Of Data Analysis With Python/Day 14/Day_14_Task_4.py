#You are given the following data, which is in list format:
# Your task is to analyze and obtain insights from this data using NumPy (do not use pandas).
# Your first task is to create one array from the three (3) lists.
# You will use this array to answer the questions that follow.
import numpy as np

names = ["Kelly","Ben","Jack","Muhammad","Jose","Liz"]
grades = [45,65,75,35,85,40]
classes = ["a","c","e","g","e","f"]

#Which student got the highest marks?

arr = np.array([names,grades,classes])
arr_T = arr.T
print("\nTransposed Array:\n",arr_T)

names_col = arr_T[:, 0]
grades_col = arr_T[:, 1].astype(int)
max_index = np.argmax(grades_col)

print("The Student WIth The Highest Mark:",names_col[max_index])

print("\nMarks Received:\n",grades_col[max_index])




