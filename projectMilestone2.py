import pandas_datareader as data
import pandas as pd
import matplotlib.pyplot as plt
import ta
from scipy import signal


#final project will have all 500 stocks but for now we are just using the first 3 for all of our sanities. 
#this is where we first get the data. We must first define our basket. 
basket = ['AAPL','ABBV','ABT']#,'ACN','ADBE','AGN','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','C','CAT','CELG','CHTR','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','USB','UTX','V','VZ','WBA','WFC','WMT','XOM']
#Then init the cluster list to hold the data that we get.
cluster = []
#loop through the tickers and get the data using pandas datareader
for ticker in basket:
  r = data.DataReader(ticker,'yahoo',start = '2006-10-09') #May need to change this based on number of rows. 
  #Assigning the ticker to the symbol column for later
  r['Symbol'] = ticker
  #appending r to the cluster list.
  cluster.append(r)
#assigning the list to a dataframe
df = pd.concat(cluster)
#sort by the dates to see all the stocks for the day
df = df.sort_index(ascending=True)
df = df.reset_index()
#print(df)

#After we get the stock prices for the stocks that we are going to use we need to add some other data points to help us predict.
#plot the trend close price
plt.plot(df['Close'])
plt.show()
#loop through the stocks in the basket
for stock in basket:
    #loop through the columns
    for col in ('Close', 'High', 'Low', 'Open', 'Volume','Adj Close'):
        #change to float
        df[col] = df[col].astype(float)
        #detrend the data
        df.loc[df['Symbol'] == stock, col] = signal.detrend(df[df['Symbol'] == stock][col])
    #make the mean close price for each stock with window of 2 and 3
    df.loc[df['Symbol'] == stock, 'mean_close_price_2'] = df.loc[df['Symbol'] == stock, 'Adj Close'].rolling(window=2).mean()
    df.loc[df['Symbol'] == stock, 'mean_close_price_3'] = df.loc[df['Symbol'] == stock, 'Close'].rolling(window=3).mean()
    #make the std close price for each stock with window of 2 and 3
    df.loc[df['Symbol'] == stock, 'std_close_price_2'] = df.loc[df['Symbol'] == stock, 'Adj Close'].rolling(window=2).std()
    df.loc[df['Symbol'] == stock, 'std_close_price_3'] = df.loc[df['Symbol'] == stock, 'Adj Close'].rolling(window=3).std()
    #make the metrics for each stocks as described in the paper
    df.loc[df['Symbol'] == stock,'RSI'] =  ta.momentum.rsi(df['Adj Close'], n = 14)
    df.loc[df['Symbol'] == stock,'STO'] = ta.momentum.stoch(df['High'], df['Low'],df['Adj Close'], n = 14)
    df.loc[df['Symbol'] == stock,'MACD'] = ta.trend.macd(df['Adj Close'], n_fast = 12, n_slow = 26)
    #create the OBV for each row
    df['OBV'] = ta.volume.on_balance_volume(df['Adj Close'], df['Volume'])

#Plot the detrended close price. verify change
plt.plot(df['Close'])
plt.show()


#Make the gain columns for the close prices
df['Tomo_gain'] = df['Adj Close'].shift(-1) - df['Adj Close']
df['Yday_gain'] = df['Tomo_gain'].shift(1)

#assign the date to the as data variable for the use of getting the day of week, quarter, and week of year.
as_date = df['Date'].dt
#get the datetime metrics
df['dayofweek'] = as_date.dayofweek
df['quarter'] = as_date.quarter
df['weekofyear'] = as_date.weekofyear
#drop NAs
df = df.dropna(axis=0)
#reset the index after the drop.
df = df.reset_index(drop=True)
#print the dataframe to validate changes
print(df)

#Test to see if the metrics were done properly
#splitting the dataframe by stock
Adf = df.where(df['Symbol'] == 'AAPL')
Adf = Adf.dropna(axis=0)
Abdf = df.where(df['Symbol']== 'ABBV')
Abdf = Abdf.dropna(axis=0)
Atdf = df.where(df['Symbol']=='ABT')
Atdf = Atdf.dropna(axis=0)
#make a subplot for the MACD and the STO metrics
plt.subplot(1,2,1)
plt.plot(Adf['MACD'])
plt.plot(Abdf['MACD'])
plt.plot(Atdf['MACD'])
plt.subplot(1,2,2)
plt.plot(Atdf['STO'])
#show the plot.
plt.show()