
import pandas as pd

#calculating column statistics
orders = pd.read_csv('orders.csv')
print(orders.head(10))
most_expensive = orders.price.max()
num_colors = orders.	shoe_color.nunique()

#.groupby() method
orders = pd.read_csv('orders.csv')
print(orders.head(10))
pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes))
