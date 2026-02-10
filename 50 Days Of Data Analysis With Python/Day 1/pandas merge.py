import pandas as pd

personal = ["Andrew","Bobby","Charlie","Dustin","Graham","Frank",]
revenue = [10000,7500,650,200,9500,12000]
bonus = [500 if r > 2500 else 0 for r in revenue]
bonus2 = [1000 if r > 5000 else 0 for r in revenue]
bonus3 = [2500 if r > 10000 else 0 for r in revenue]



monthly_sales = pd.DataFrame({"Employee":personal,"Total Revenue":revenue,"Bonus":bonus,"Bonus 2":bonus2,"Bonus 3":bonus3})

print(monthly_sales)