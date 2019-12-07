#Sourced from 
##############################################
##https://github.com/pskrunner14/trading-bot##
##############################################

import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import logging
import coloredlogs

from train import *
from evaluate import show_eval_result


train_stock = 'C:/Users/brand/OneDrive/Documents/trading-bot-master/trading-bot-master/data/GOOGL.csv'
val_stock = 'C:/Users/brand/OneDrive/Documents/trading-bot-master/trading-bot-master/data/GOOGL_2018.csv'
window_size = 10
batch_size = 16
ep_count = 200
model_name = 'model_GOOGL'
pretrained = False
debug = False

df = pd.read_csv(val_stock)

# filter out the desired features
df = df[['Date', 'Adj Close']]

# rename feature column names
df = df.rename(columns={'Adj Close': 'actual', 'Date': 'date'})

df.head()

dates = df['date']
dates = pd.to_datetime(dates, infer_datetime_format=True)
df['date'] = dates

df.info()
df.head()

def visualize(df, history):
    # add history to dataframe
    position = [history[0][0]] + [x[0] for x in history]
    actions = ['HOLD'] + [x[1] for x in history]
    df['position'] = position
    df['action'] = actions
    
    # specify y-axis scale for stock prices
    scale = alt.Scale(domain=(min(min(df['actual']), min(df['position'])) - 50, max(max(df['actual']), max(df['position'])) + 50), clamp=True)
    
    # plot a line chart for stock positions
    actual = alt.Chart(df).mark_line(
        color='green',
        opacity=0.5
    ).encode(
        x='date:T',
        y=alt.Y('position', axis=alt.Axis(format='$.2f', title='Price'), scale=scale)
    ).interactive(
        bind_y=False
    )
    
    # plot the BUY and SELL actions as points
    points = alt.Chart(df).transform_filter(
        alt.datum.action != 'HOLD'
    ).mark_point(
        filled=True
    ).encode(
        x=alt.X('date:T', axis=alt.Axis(title='Date')),
        y=alt.Y('position', axis=alt.Axis(format='$.2f', title='Price'), scale=scale),
        color='action'
        #color=alt.Color('action', scale=alt.Scale(range=['blue', 'red']))
    ).interactive(bind_y=False)

    # merge the two charts
    chart = alt.layer(actual, points, title=val_stock).properties(height=300, width=1000)
    
    return chart

coloredlogs.install(level='DEBUG')
switch_k_backend_device()

agent = Agent(window_size, pretrained=pretrained, model_name=model_name)
train_data = get_stock_data(train_stock)
val_data = get_stock_data(val_stock)

initial_offset = val_data[1] - val_data[0]

for i in range(1, ep_count + 1):
    train_result = train_model(agent, i, train_data, ep_count=ep_count,
                                batch_size=batch_size, window_size=window_size)
    val_result, _ = evaluate_model(agent, val_data, window_size, debug)
    show_train_result(train_result, val_result, initial_offset)
    
val_result, history = evaluate_model(agent, val_data, window_size, debug)
show_eval_result(model_name, val_result, initial_offset)
chart = visualize(df, history)
chart