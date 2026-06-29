#For this challenge, you are going to preprocess, analyze, and create visualizations of the toys_sales_data dataset.
#Here is a snippet of the dataset below:

#2 Using Matplotlib, plot a bar plot of the sales value of each item.
#Your plot should have axis labels and a title. The plot size should be 10 inches by 8 inches.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('toys_sales_data.csv')

# Convert Total Sales to numeric (if needed)
df['Total Sales'] = (
    df['Total Sales']
    .replace(r'[\$,]', '', regex=True)
    .astype(float)
)

# Create a bar plot
plt.figure(figsize=(10, 8))
plt.bar(df['Item'], df['Total Sales'])

# Add title and axis labels
plt.title('Total Sales by Item')
plt.xlabel('Item')
plt.ylabel('Total Sales')

# Rotate x-axis labels if necessary
plt.xticks(rotation=45)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()