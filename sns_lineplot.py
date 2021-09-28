#Standard

import numpy as np

import pandas as pd

from numpy.random import randn

from pandas import Series, DataFrame

#Stats

from scipy import stats

#Matplotlib

import matplotlib as mpl

import matplotlib.pyplot as plt

#Seaborn

import seaborn as sns

#Draw

sns.set() #設定繪圖改為seaborn繪製

# df = pd.DataFrame({ '2020':[100, 110, 120],
#                     '2021':[110, 100, 150],
#                     '2022':[90, 130, 110]}
#                     , index=['ProductA','ProductB','ProductC'])

df = pd.DataFrame({ 'Year':['2020', '2021', '2022', '2020', '2021', '2022', '2020', '2021', '2022'],
                    'Product':['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
                    'Price':[100, 110, 120, 110, 100, 150, 90, 130, 110]})

# df = df.pivot('Year','Product','Price')

print(df)


flights = sns.load_dataset("flights")
flights_wide = flights.pivot("year", "month", "passengers")
print(flights_wide)

sns.lineplot(data=df, x='Year', y='Price', hue="Product")

# plt.xlabel('this is x')

# plt.ylabel('this is y')

# plt.title('this is a demo')

# plt.legend()

plt.show() #繪圖