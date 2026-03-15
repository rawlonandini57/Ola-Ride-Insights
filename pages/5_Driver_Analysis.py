import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("OLA_Ride_Data_Sheet.csv")

st.title("🚖 Driver Performance Analysis")

driver_ratings = df.groupby("Driver_ID")["Driver_Ratings"].mean().reset_index()

fig = px.bar(
    driver_ratings.head(10),
    x="Driver_ID",
    y="Driver_Ratings",
    title="Top Drivers by Rating"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Driver Rating Distribution")

fig2 = px.histogram(df, x="Driver_Ratings")

st.plotly_chart(fig2)
