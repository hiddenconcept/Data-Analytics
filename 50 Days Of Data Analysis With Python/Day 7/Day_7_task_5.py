players = ["Robin","Leo","Pogba","Diego","Ronaldo"]
teams = ["Man UTD","Barca","Juve","Napo","Rmadrid"]

goals =[[12,15,16,15,13],
        [26,30,31,25,24],
        [10,12,8,6,13],
        [18,19,17,20,21],
        [21,32,25,21,22]
        ]

#Each row in the "goals" list represents the goals scored by
#each player in the last 5 seasons. For example, Robin’s
#goals are [12, 15, 16, 15, 13] and he plays for "Man UTD,"
#and Leo's are [26, 30, 31, 25, 24] and he plays for "Barca."
#Using NumPy, Seaborn, and Matplotlib, create a heatmap
#of the goals and calculate the gradient of the data.
#Annotate your heat map. The x-ticks will be the names of
#the players, and the y-ticks will be the teams of the player

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

scores = np.array(goals)
gradient = np.gradient(scores)

print("\nThe Goals Array:\n",scores)
print("\nThe Gradient Array:\n",gradient)

#heatmap

plt.figure(figsize=(10,10))
sns.heatmap(scores, annot=True, fmt="d", cmap="YlGnBu",xticklabels=players, yticklabels=teams)
plt.title("Goals Scored by Players This Season")
plt.xlabel("Player")
plt.ylabel("Team")
plt.show()

