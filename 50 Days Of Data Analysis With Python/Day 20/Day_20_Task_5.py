# Using pandas, calculate the average cost per product.

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

# Calculate average cost
average_cost = df['Cost'].mean()
print(f"Average Cost per Product: ${average_cost:,.2f}")