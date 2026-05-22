import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

##Example 4: Let us illustrate the distribution of heights of 200 people using a histogram


#Here we will concentrate on heights which are 160 and the standard deviation is 11
heights_array = np.random.normal(160, 11, 200)
## Use plotly express histogram chart function px.histogram.Provide input data x to the histogram
fig = px.histogram(x=heights_array,title="Distribution of Heights")
fig.show()