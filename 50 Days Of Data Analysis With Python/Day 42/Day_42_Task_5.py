#For this challenge, you are going to preprocess, analyze, and create visualizations of the toys_sales_data dataset.
#Here is a snippet of the dataset below:

#5 Use Seaborn to create a scatter plot showing the relationship between items and the quantity of each item.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('toys_sales_data.csv')

# Convert Total Sales to numeric
df['Total Sales'] = (
    df['Total Sales']
    .replace(r'[$,]', '', regex=True)
    .astype(float)
)

# Create a scatter plot
plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x='Item', y='Quantity', s=100)

# Add title and labels
plt.title('Relationship Between Items and Quantity')
plt.xlabel('Item')
plt.ylabel('Quantity')

# Display the plot
plt.tight_layout()
plt.show()