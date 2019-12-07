# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:27:20 2019

@author: brand
"""
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import pandas_datareader as data
sp100 = ['AAPL','ABBV','ABT','ACN','ADBE','AGN','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','C','CAT','CELG','CHTR','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','USB','UTX','V','VZ','WBA','WFC','WMT','XOM']
sp5 = ['AIG','C','T','CVS','MMM']
googl = ['GOOGL']
r = data.DataReader(sp100,'yahoo',start = '2017-08-10')#, end = '2018-08-10')
r = r['Close']

mu = expected_returns.ema_historical_return(r)
shrink = risk_models.CovarianceShrinkage(r)
S = shrink.ledoit_wolf()

ef = EfficientFrontier(mu, S)
weights = ef.efficient_risk(target_risk=0.10)

#print(weights)
ef.portfolio_performance(verbose=True)

from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
latest_prices = get_latest_prices(r)

da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=1000)
allocation, leftover = da.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds remaining: ${:.2f}".format(leftover))

portfolio = allocation
print(allocation)
starting_cash = leftover