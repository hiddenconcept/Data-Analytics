#You are going to analyze the sales data of a spare parts business.
#You are going to use the spare_parts.csv dataset.

#8 Use a Seaborn barplot to visualize the distribution of quantities for each item.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spare_parts.csv")

# Create barplot
sns.barplot(
    data=df,
    x='spare_part',
    y='quantity'
)

# Labels and title
plt.title('Quantity Distribution by Spare Part')
plt.xlabel('Spare Part')
plt.ylabel('Quantity')

plt.show()