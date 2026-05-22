import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

##Example 3: Let us illustrate the average pass percentage of classes from grade 6 to grade 10

# Define an array containing number of bicycles sold

score_array=[80,90,56,88,95]

grade_array=['Grade 6','Grade 7','Grade 8','Grade 9','Grade 10']

fig = px.bar( x=grade_array, y=score_array, title='Pass Percentage of Classes')

fig.show()