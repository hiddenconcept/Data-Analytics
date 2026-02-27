#You are given the following data, which is in list format:
# Your task is to analyze and obtain insights from this data using NumPy (do not use pandas).
# Your first task is to create one array from the three (3) lists.
# You will use this array to answer the questions that follow.
import numpy as np

names = ["Kelly","Ben","Jack","Muhammad","Jose","Liz"]
grades = [45,65,75,35,85,40]
classes = ["a","c","e","g","e","f"]

#3.	Write code that returns how many marks a student named Liz got.

print("Names of students are:",names)
print("Grades of students are:",grades)
print("Classes are:",classes)

arr = np.array([names, grades, classes])
print("\n3 Dimension Array:\n",arr)

arr_T = arr.T
print("\nTransposed Array:\n",arr_T)
# Extract individual columns
names_col   = arr_T[:, 0]
grades_col  = arr_T[:, 1].astype(int)
classes_col = arr_T[:, 2]
lizzie = names[-1]
mask = names_col == "Liz"
filtered = arr_T[mask]

print("Liz's Record:\n",filtered)
print("\nMarks by Liz:",int(filtered[0,1]))




