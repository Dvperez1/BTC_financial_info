import krakenex
from pykrakenapi import KrakenAPI
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

#financial_variable = [Volume,Price,VWAP]
api = krakenex.API()
k = KrakenAPI(api)

data = ohlc, last = k.get_ohlc_data("BTCUSD", interval=1)
df = data[0]

global price
price = df.loc[:,'open']
global volume
volume = df.loc[:,'volume']
global VWAP
VWAP = df.loc[:,'vwap']
global date
date = df.index


def main():
    date = df.index
    container = st.container()
    container.header("Bitcoin Financial Data for the past 12 hours")
    container.write(
        "This chart shows the financial data of the cryptocurrency Bitcoin(BTC), based on volume, price in USD, and Volume Weighted Average Price (VWAP) ")
    st.write("Use the dropdown menu to choose Volume, VWAP, or Price.")
    y_options = ['volume', 'high','low','count']
    y_axis = st.selectbox("Choose your financial variable:", y_options)
    x_axis = (date)
    visualize_data(df, x_axis, y_axis)


def visualize_data(df, x_axis, y_axis):
    graph = go.Figure(px.line(df,x_axis,y_axis,labels={"dtime":"Date and time"},title="Bitcoin Data"))
    st.plotly_chart(graph)

    graph2 = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

    graph2.update_layout(
        title="Bitcoin VWAP",
        xaxis_title="Date and Time",
        yaxis_title="US Dollars")

    st.plotly_chart(graph2)
    st.write('Financial Data Chart')
    st.dataframe(df)






# Calculated VWAP but I did use the vwap already in the dataframe for the graphs
psum = sum(price)
vsum = sum(volume)

for index, value in volume.items():
    vwap = psum * value /vsum
    vwap_list = []
    vwap_list.append(vwap)

#options

line_graph = px.line(
  # Set the appropriate DataFrame and title
  data_frame=df, title=f'Bitcoin over 12 hour period',
  # Set the x and y arguments
  x=df.index, y='volume', markers=True, facet_col_spacing=0.5)

scatter_graph = px.scatter(
  # Set the appropriate DataFrame and title
  data_frame=df, title='Bitcoin VWAP over 12 hour period',
  # Set the x and y arguments
  x=df.index, y=['vwap'], width=850, height=500)

if __name__ == "__main__":
    main()



