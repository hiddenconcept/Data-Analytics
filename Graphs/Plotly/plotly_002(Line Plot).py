import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

##Example 2: Let us illustrate the sales of bicycles from Jan to August last year using a line chart

# Define an array containing number of bicycles sold

number_of_bicycles_sold_array=[50,100,40,150,160,70,60,45]

# Define an array containing months
months_array=["Jan","Feb","Mar","April","May","June","July","August"]

fig = go.Figure()

fig.add_trace(go.Scatter(x=months_array, y=number_of_bicycles_sold_array, mode='lines', marker=dict(color='green')))

fig.update_layout(title='Bicycle Sales', xaxis_title='Months', yaxis_title='Number of Bicycles Sold')

fig.show()