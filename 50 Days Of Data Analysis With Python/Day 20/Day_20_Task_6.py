# Using pandas, calculate the average profit per product.

products = ["Sugar","Salt","Oil","Diapers","Rice"]
costs = [2450,1989,6745,9807,8743]
sales = [27908,4508,6743,9976,9000]

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Product': products,
    'Cost': costs,
    'Sales': sales
})

# Calculate profit
df['Profit'] = df['Sales'] - df['Cost']

# Calculate average profit
average_profit = df['Profit'].mean()
print(f"Average Profit per Product: ${average_profit:,.2f}")