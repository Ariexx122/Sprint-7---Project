import streamlit as st
import plotly.graph_objects as go
import pandas as pd


car_data = pd.read_csv(
    r"C:\Users\ariex\OneDrive\Documents\Repositories\Sprint-7---Project\vehicles_us.csv")

st.header("Car Sale Ads Data Visualization")

st.write("This is a simple Streamlit app to visualize car sale ads data.")

build_histogram = st.checkbox('Build a histogram')

if build_histogram:
    st.write("Creating a histogram for the dataset of car sale ads.")
    fig = go.Figure(data=go.Histogram(x=car_data['odometer']))
    fig.update_layout(title_text='Odometer Distribution')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Build a scatter plot')

if build_scatter:
    st.write("Creating a scatter plot for the dataset of car sale ads.")
    fig = go.Figure(data=go.Scatter(x=car_data.index,
                    y=car_data['odometer'], mode='markers'))
    fig.update_layout(title_text='Odometer Scatter Plot')
    st.plotly_chart(fig, use_container_width=True)
