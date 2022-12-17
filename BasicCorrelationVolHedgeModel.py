#BasicNotionalHedgingVol
import yfinance as yf
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts
from matplotlib import pyplot as plt
import statistics
import math

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

# stock volatility calculations
close = data["Adj Close"]
log = np.log(close/close.shift())
vol = log.std()*252**.5
volatility = pd.DataFrame(vol)

#ticker to be hedged
df2 = pd.DataFrame(data=x)
ticker = "TSLA"


bigdata = pd.concat([df2[ticker],volatility], axis=1, ignore_index=True)
volcorr = bigdata.nsmallest(hedge_base,0)
adjvalue = volcorr.multiply(position_size)
nothedge = adjvalue.divide(hedge_base)

#output notional to hedge with based on correlation or volatility
nothedge