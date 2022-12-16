#Hedging
import yfinance as yf
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts
from matplotlib import pyplot as plt

# amount of tickers used to hedge
hedge_base = int(input())
# notional to be hedged
position_size = float(input())

# Read and print the stock tickers that make up S&P500
tickers = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]


symbol = tickers['Symbol']
symbol.head()

# Get the data for this tickers from yahoo finance
data = yf.download(tickers.Symbol.to_list(),'2022-1-1','2022-12-31')
data.head()
df = pd.DataFrame(data=data)

x=df["Close"].corr()
matrix = np.triu(x)
df2 = pd.DataFrame(data=x)
name = 'TSLA'

y = df2.nlargest(hedge_base+1,[name])
for row in y.index:
    print(row, end= " ")
y[name]

z = df2.nsmallest(hedge_base,[name])
for row in z.index:
    print(row, end= " ")

df3 = z[name]
adjusted_values = df3.multiply(position_size)
notionalhedge = adjusted_values.divide(hedge_base*-1)
#shows amount of notional to hedge for each stock
notionalhedge