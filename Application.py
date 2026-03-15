import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="OLA Ride Insights", layout="wide")

st.title("🚖 OLA Ride Analytics Dashboard")
st.markdown("Interactive dashboard for analyzing ride-sharing data.")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("OLA_Ride_Data_Sheet.csv")
    return df

df = load_data()

st.sidebar.header("Filters")

# Vehicle filter
vehicle_type = st.sidebar.multiselect(
    "Select Vehicle Type",
    options=df["Vehicle_Type"].unique(),
    default=df["Vehicle_Type"].unique()
)

df = df[df["Vehicle_Type"].isin(vehicle_type)]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bookings", len(df))
col2.metric("Total Revenue", f"₹{df['Booking_Value'].sum():,.0f}")
col3.metric("Average Ride Distance", f"{df['Ride_Distance'].mean():.2f} km")
col4.metric("Avg Driver Rating", f"{df['Driver_Ratings'].mean():.2f}")

st.divider()

# Ride Volume Over Time
st.subheader("📈 Ride Volume Over Time")

rides_by_date = df.groupby("Date")["Booking_ID"].count().reset_index()

fig = px.line(
    rides_by_date,
    x="Date",
    y="Booking_ID",
    title="Daily Ride Volume"
)

st.plotly_chart(fig, use_container_width=True)

# Booking Status
st.subheader("📊 Booking Status Breakdown")

status_counts = df["Booking_Status"].value_counts().reset_index()
status_counts.columns = ["Status", "Count"]

fig2 = px.pie(
    status_counts,
    values="Count",
    names="Status",
    title="Booking Status Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# Vehicle Type Analysis
st.subheader("🚗 Ride Distance by Vehicle Type")

vehicle_distance = df.groupby("Vehicle_Type")["Ride_Distance"].mean().reset_index()

fig3 = px.bar(
    vehicle_distance,
    x="Vehicle_Type",
    y="Ride_Distance",
    color="Vehicle_Type",
    title="Average Ride Distance per Vehicle Type"
)

st.plotly_chart(fig3, use_container_width=True)

# Revenue by Payment Method
st.subheader("💳 Revenue by Payment Method")

payment_revenue = df.groupby("Payment_Method")["Booking_Value"].sum().reset_index()

fig4 = px.bar(
    payment_revenue,
    x="Payment_Method",
    y="Booking_Value",
    color="Payment_Method",
    title="Revenue by Payment Method"
)

st.plotly_chart(fig4, use_container_width=True)

# Ratings
st.subheader("⭐ Driver Ratings Distribution")

fig5 = px.histogram(
    df,
    x="Driver_Ratings",
    nbins=10,
    title="Driver Ratings Distribution"
)

st.plotly_chart(fig5, use_container_width=True)

# Top Customers
st.subheader("🏆 Top Customers by Booking Value")

top_customers = df.groupby("Customer_ID")["Booking_Value"].sum().nlargest(5).reset_index()

fig6 = px.bar(
    top_customers,
    x="Customer_ID",
    y="Booking_Value",
    title="Top 5 Customers"
)

st.plotly_chart(fig6, use_container_width=True)

st.divider()

st.subheader("📋 Raw Dataset")

st.dataframe(df)
