import pandas as pd
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]
items = pd.DataFrame(items2, index = ["store1", "store2"])

x = items.isnull()#.sum().sum()
print(x)
y = items.count()
print(y)
z = items.isnull().sum().sum()
print(z)