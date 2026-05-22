import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

##Example 1: Let us illustrate the income vs age of people in a scatter plot

age_array = np.random.randint(25,55,60)

income_array = np.random.randint(300000,700000,3000000)

fig=go.Figure()

fig.add_trace(go.Scatter(x=age_array, y=income_array, mode='markers', marker=dict(color='blue')))

fig.update_layout(title='Economic Survey', xaxis_title='Age', yaxis_title='Income')

fig.show()