#You are given the following data, which is in list format:
# Your task is to analyze and obtain insights from this data using NumPy (do not use pandas).
# Your first task is to create one array from the three (3) lists.
# You will use this array to answer the questions that follow.
import numpy as np

names = ["Kelly","Ben","Jack","Muhammad","Jose","Liz"]
grades = [45,65,75,35,85,40]
classes = ["a","c","e","g","e","f"]

#1.	Using NumPy, write code that returns all the names and the  number of  students from class "e" who got over 50 marks.

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

# Filter: class "e" AND grade > 50
mask = (classes_col == "e") & (grades_col > 50)

filtered = arr_T[mask]

print("\nStudents from class 'e' with over 50 marks:")
print(filtered)
print("\nNames:", filtered[:, 0])
print("Number of students:", len(filtered))

