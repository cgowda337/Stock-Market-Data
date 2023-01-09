# Import packages
import yfinance as yf
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts
from matplotlib import pyplot as plt
import statistics
import math

#download data for open & close
fut_list = ['SPY','TLT']
data= yf.download(fut_list, start="2017-01-01", end="2023-01-10")[['Open','Adj Close']]
df = pd.DataFrame(data=data)

#calculate 20d standard dev
diff = df['Open']-df['Adj Close']
daily_returns = diff['SPY']+diff['TLT']
daily_df = pd.DataFrame(data=daily_returns)
rpar = np.log(np.absolute(daily_df.tail(20).pct_change(1)))
x = math.exp(rpar.std()*240**0.5)

#download data for close
fut_list = ['SPY','TLT']
data2= yf.download(fut_list, start="2017-01-01", end="2023-01-10")['Adj Close']
df2 = pd.DataFrame(data=data2['SPY']+data2['TLT'])

#volatility calculation
log = np.log(df2/df2.shift())
vol = log.rolling(20).std()*252**.5
volatility = pd.DataFrame(data = vol)

#plot system leverage
leverage = (x/volatility)
leverage.plot()
