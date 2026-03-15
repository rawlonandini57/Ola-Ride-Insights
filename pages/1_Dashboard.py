import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("OLA_Ride_Data_Sheet.csv")

st.title("📊 Ride Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bookings", len(df))
col2.metric("Total Revenue", f"₹{df['Booking_Value'].sum():,.0f}")
col3.metric("Avg Ride Distance", f"{df['Ride_Distance'].mean():.2f} km")
col4.metric("Avg Driver Rating", f"{df['Driver_Ratings'].mean():.2f}")

st.subheader("Ride Demand Over Time")

rides = df.groupby("Date")["Booking_ID"].count().reset_index()

fig = px.line(rides, x="Date", y="Booking_ID")

st.plotly_chart(fig, use_container_width=True)
