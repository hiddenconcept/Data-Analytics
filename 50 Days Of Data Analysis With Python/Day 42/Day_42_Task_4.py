#For this challenge, you are going to preprocess, analyze, and create visualizations of the toys_sales_data dataset.
#Here is a snippet of the dataset below:

#4 Using Matplotlib subplots, plot both a bar plot and a line plot showing the total sales for each item.
# Your subplot must have one column and two rows. The line plot must be on top.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('toys_sales_data.csv')

# Convert Total Sales to numeric
df['Total Sales'] = (
    df['Total Sales']
    .replace(r'[$,]', '', regex=True)
    .astype(float)
)

# Create subplots (2 rows, 1 column)
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Line plot (top)
axes[0].plot(df['Item'], df['Total Sales'], marker='o')
axes[0].set_title('Total Sales by Item (Line Plot)')
axes[0].set_xlabel('Item')
axes[0].set_ylabel('Total Sales')

# Bar plot (bottom)
axes[1].bar(df['Item'], df['Total Sales'])
axes[1].set_title('Total Sales by Item (Bar Plot)')
axes[1].set_xlabel('Item')
axes[1].set_ylabel('Total Sales')

# Adjust spacing between plots
plt.tight_layout()

# Display the plots
plt.show()