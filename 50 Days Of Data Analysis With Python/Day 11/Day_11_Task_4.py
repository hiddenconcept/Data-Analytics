import numpy as np

student_id = [1,2,3,4,5,6,7,8,9,10]
attendance = [85,92,70,95,80,60,90,75,65,100]
final_exam_score = [ 80,89,65,56,66,50,85,70,55,100]


#Using NumPy, create an array using the lists above. Each list must be a row in the array. Your array must have 3 rows and 10 columns.
# To visualize the correlation between attendance and the final_exam_score, create a scatter plot using Matplotlib.
# Set the final_exam_score the x-axis and attendance as the y-axis of your scatter plot.
# Use the NumPy array you just created as the source of your data for the plot.


#b. By visualizing your scatter plot (question 4a), what final score was the outlier of the data?


import numpy as np
import matplotlib.pyplot as plt

arr =np.array([student_id,attendance,final_exam_score])

plt.scatter(arr[2],arr[1])
plt.title('Final Exam Score vs. Attendance')
plt.xlabel('Final Exam Score')
plt.ylabel('Attendance')
plt.show()

print("\nThe Outlier is:\n", "56")



