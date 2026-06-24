#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts.csv dataset.

#6 Use a 3D scatter plot to visualize the relationship between price, quantity, and cost for each item.
#Use Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Convert columns to numeric
df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['costs'] = pd.to_numeric(df['costs'], errors='coerce')

# Remove rows with missing values
df = df.dropna(subset=['sale_price', 'quantity', 'costs'])

# Create 3D figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create scatter plot
ax.scatter(
    df['sale_price'],
    df['quantity'],
    df['costs']
)

# Labels and title
ax.set_xlabel('Sale Price')
ax.set_ylabel('Quantity')
ax.set_zlabel('Cost')
ax.set_title('3D Scatter Plot: Sale Price vs Quantity vs Cost')

plt.show()