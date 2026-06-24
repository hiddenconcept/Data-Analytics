#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts.csv dataset.

#10 Use a Seaborn lmplot to fit a linear regression model
#Visualize the relationship between price and total revenue.
#Your plot should have a white grid style and a height of 8 inches.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Clean total_revenue column
df['total_revenue'] = (
    df['total_revenue']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# Set white grid style
sns.set_style("whitegrid")

# Create lmplot
sns.lmplot(
    data=df,
    x='sale_price',
    y='total_revenue',
    height=8
)

# Labels and title
plt.title('Relationship Between Price and Total Revenue')
plt.xlabel('Price')
plt.ylabel('Total Revenue')

plt.show()