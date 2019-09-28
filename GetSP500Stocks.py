# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 04:48:41 2019

@author: brand
"""
import pandas_datareader as data
import pandas as pd
basket = ['AAPL','ABBV','ABT','ACN','ADBE','AGN','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','C','CAT','CELG','CHTR','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','USB','UTX','V','VZ','WBA','WFC','WMT','XOM']


cluster = []
for ticker in basket:
  r = data.DataReader(ticker,'yahoo',start = '2012-09-21')
  r['Symbol'] = ticker
  cluster.append(r)
df = pd.concat(cluster)
df = df.sort_index(ascending=True)
df = df.reset_index()
print(df)
