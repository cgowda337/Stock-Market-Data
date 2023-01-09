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

#target volatility
target_vol = 0.125

#download data for close
fut_list = ['SPY','IEF']
data2= yf.download(fut_list, start="2009-01-01", end="2023-01-10")['Adj Close']
df2 = pd.DataFrame(data=(data2['SPY']*0.6)+(data2['IEF']*0.4))

#20 day annualized volatility calculation
vol = pd.DataFrame(data=(((df2.pct_change(1).rolling(20)).std()))*(252**0.5))
vol

leverage = target_vol/vol
np.clip(leverage, 0, 2).plot(legend=None)
plt.title('Leverage(12.5% Vol Target)')
plt.xlabel('Date')
plt.ylabel('Leverage')
