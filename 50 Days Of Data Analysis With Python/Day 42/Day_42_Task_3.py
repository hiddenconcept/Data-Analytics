#For this challenge, you are going to preprocess, analyze, and create visualizations of the toys_sales_data dataset.
#Here is a snippet of the dataset below:

#3 Using pandas and Matplotlib, plot a pie chart showing the percentage of total sales for each item.
# Your plot should have a title.
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

# Create a pie chart
plt.figure(figsize=(8, 8))
df.set_index('Item')['Total Sales'].plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

# Add title
plt.title('Percentage of Total Sales for Each Item')

# Remove the y-axis label
plt.ylabel('')

# Display the plot
plt.tight_layout()
plt.show()