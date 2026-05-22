import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

## Monthly expenditure of a family
# Random Data
exp_percent= [20, 50, 10,8,12]
house_holdcategories = ['Grocery', 'Rent', 'School Fees','Transport','Savings']

# Use px.pie function to create the chart. Input dataset.
# Values parameter will set values associated to the sector. 'exp_percent' feature is passed to it.
# labels for the sector are passed to the `house hold categoris` parameter.
fig = px.pie(values=exp_percent, names=house_holdcategories, title='Household Expenditure')
fig.show()
