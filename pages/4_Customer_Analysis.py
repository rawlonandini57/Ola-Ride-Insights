import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("OLA_Ride_Data_Sheet.csv")

st.title("👥 Customer Analytics")

top_customers = df.groupby("Customer_ID")["Booking_Value"].sum().nlargest(10).reset_index()

fig = px.bar(
    top_customers,
    x="Customer_ID",
    y="Booking_Value",
    title="Top Customers by Revenue"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Customer Ratings Distribution")

fig2 = px.histogram(df, x="Customer_Rating")

st.plotly_chart(fig2)
