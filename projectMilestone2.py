import pandas_datareader as data
import pandas as pd
import matplotlib.pyplot as plt
import ta
from scipy import signal


#final project will have all 500 stocks but for now we are just using the first 3 for all of our sanities. 
basket = ['AAPL','ABBV','ABT']#,'ACN','ADBE','AGN','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','C','CAT','CELG','CHTR','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','USB','UTX','V','VZ','WBA','WFC','WMT','XOM']

cluster = []
for ticker in basket:
  r = data.DataReader(ticker,'yahoo',start = '2006-10-09') #May need to change this based on number of rows. 
  r['Symbol'] = ticker
  cluster.append(r)
df = pd.concat(cluster)
df = df.sort_index(ascending=True)
df = df.reset_index()
#print(df)

#After we get the stock prices for the stocks that we are going to use we need to add some other data points to help us predict.

for stock in basket:
    for col in ('Close', 'High', 'Low', 'Open', 'Volume','Adj Close'):
        df[col] = df[col].astype(float)
        df.loc[df['Symbol'] == stock, col] = signal.detrend(df[df['Symbol'] == stock][col])
    df.loc[df['Symbol'] == stock, 'mean_close_price_2'] = df.loc[df['Symbol'] == stock, 'Close'].rolling(window=2).mean()
    df.loc[df['Symbol'] == stock, 'mean_close_price_3'] = df.loc[df['Symbol'] == stock, 'Close'].rolling(window=3).mean()
    df.loc[df['Symbol'] == stock, 'std_close_price_2'] = df.loc[df['Symbol'] == stock, 'Close'].rolling(window=2).std()
    df.loc[df['Symbol'] == stock, 'std_close_price_3'] = df.loc[df['Symbol'] == stock, 'Close'].rolling(window=3).std()
    df['OBV'] = ta.volume.on_balance_volume(df['Adj Close'], df['Volume'])
    df['RSI'] =  ta.momentum.rsi(df['Adj Close'], n = 14)
    df['STO'] = ta.momentum.stoch(df['High'], df['Low'],df['Adj Close'], n = 14)
    df['MACD'] = ta.trend.macd(df['Adj Close'], n_fast = 12, n_slow = 26)


    
df['Tomo_gain'] = df['Close'].shift(-1) - df['Close']
df['Yday_gain'] = df['Tomo_gain'].shift(1)

as_date = df['Date'].dt
df['dayofweek'] = as_date.dayofweek
df['quarter'] = as_date.quarter
df['weekofyear'] = as_date.weekofyear
df = df.dropna(axis=0)
df = df.reset_index(drop=True)
#print(df)
#stockdf = StockDataFrame.retype(df)

#Test to see if the metrics were done properly

Adf = df.where(df['Symbol'] == 'AAPL')
Adf = Adf.dropna(axis=0)
Abdf = df.where(df['Symbol']== 'ABBV')
Abdf = Abdf.dropna(axis=0)
Atdf = df.where(df['Symbol']=='ABT')
Atdf = Atdf.dropna(axis=0)
plt.subplot(1,2,1)
plt.plot(Adf['MACD'])
plt.plot(Abdf['MACD'])
plt.plot(Atdf['MACD'])
plt.subplot(1,2,2)
plt.plot(Adf['STO'])
plt.show()