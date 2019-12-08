import pandas_datareader as data
import pandas as pd
import matplotlib.pyplot as plt
import ta
import seaborn as sns

df = data.DataReader('GOOGL','yahoo',start='2017-01-01')
#make the metrics for each stocks as described in the paper
df['RSI'] =  ta.momentum.rsi(df['Adj Close'], n = 14)
df['STO'] = ta.momentum.stoch(df['High'], df['Low'],df['Adj Close'], n = 14)
df['MACD'] = ta.trend.macd(df['Adj Close'], n_fast = 12, n_slow = 26)
#create the OBV for each row
df['OBV'] = ta.volume.on_balance_volume(df['Adj Close'], df['Volume'])
df['change'] = df['Adj Close'].pct_change(1)
 
df = df.dropna()

print(df['Adj Close'].describe())
print(df['change'].describe())
plt.plot(df['High'])
plt.plot(df['Low'])
plt.plot(df['Open'])
plt.plot(df['Close'])
plt.show()

sns.distplot(df['change'])
plt.figure()
corr = df.corr()
sns.heatmap(corr)


