import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

ticker = 'META'
start = dt.datetime(2020,1,1)
end =  dt.datetime(2022,1,1)
data = yf.download(ticker, start , end)
delta = data['Adj Close'].diff(1)
delta.dropna(inplace=True)

positve = delta.copy()
negative = delta.copy()

positve[positve<0]=0
negative[negative>0]=0

days = 14

average_gain = positve.rolling(window=days).mean()
average_loss = abs(negative.rolling(window=days).mean())

relative_strength = average_gain/average_loss
RSI = 100.0 - (100.0/(1.0 + relative_strength))

combined = pd.DataFrame()
combined['Adj Close'] = data['Adj Close']
combined['RSI'] = RSI

plt.figure(figsize=(12,8))
ax1 = plt.subplot(211)
ax1.plot(combined.index, combined['Adj Close'], color='lightgrey')
ax1.set_title('Adjusted Closed Price', color='white')
ax1.grid(True, color='#555555')
ax1.set_axisbelow(True)
ax1.set_facecolor('black')
ax1.figure.set_facecolor('#121212')
ax1.tick_params(axis='x',colors='white')
ax1.tick_params(axis='y',colors='white')

ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(combined.index, combined['RSI'], color='lightgrey')
ax2.axhline(0,linestyle='--', alpha=0.5, color='#ff0000')
ax2.axhline(10,linestyle='--', alpha=0.5, color='#ffaa00')
ax2.axhline(20,linestyle='--', alpha=0.5, color='#00ff00')
ax2.axhline(30,linestyle='--', alpha=0.5, color='#cccccc')
ax2.axhline(70,linestyle='--', alpha=0.5, color='#cccccc')
ax2.axhline(80,linestyle='--', alpha=0.5, color='#00ff00')
ax2.axhline(90,linestyle='--', alpha=0.5, color='#ffaa00')
ax2.axhline(100,linestyle='--', alpha=0.5, color='#ff0000')

ax2.set_title('RSI Value', color='white')
ax2.grid(False)
ax2.set_axisbelow(True)
ax2.set_facecolor('black')
ax2.tick_params(axis='x',colors='white')
ax2.tick_params(axis='y',colors='white')

plt.show()