import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

##Example 5: Let us illustrate crime statistics of US cities with a bubble chart

# Create a dictionary having city,numberofcrimes and year as 3 keys
crime_details = {
    'City': ['Chicago', 'Chicago', 'Austin', 'Austin', 'Seattle', 'Seattle'],
    'Numberofcrimes': [1000, 1200, 400, 700, 350, 1500],
    'Year': ['2007', '2008', '2007', '2008', '2007', '2008'],
}

# create a Dataframe object with the dictionary
df = pd.DataFrame(crime_details)

## Group the number of crimes by city and find the total number of crimes per city
bub_data = df.groupby('City')['Numberofcrimes'].sum().reset_index()

## Bubble chart using px.scatter function with x ,y and size varibles defined.Title defined as Crime Statistics
fig = px.scatter(bub_data, x="City", y="Numberofcrimes", size="Numberofcrimes",
                 hover_name="City", title='Crime Statistics', size_max=60)
fig.show()