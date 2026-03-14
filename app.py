import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="OLA Ride Insights", layout="wide")

st.title("🚕 OLA Ride Insights Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("OLA_Ride_Data_Sheet.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

pickup_location = st.sidebar.multiselect(
    "Select Pickup Location",
    options=df["Pickup_Location"].unique(),
    default=df["Pickup_Location"].unique()
)

vehicle = st.sidebar.multiselect(
    "Select Vehicle Type",
    options=df["Vehicle_Type"].unique(),
    default=df["Vehicle_Type"].unique()
)

df_filtered = df[(df["Pickup_Location"].isin(pickup_location)) & (df["Vehicle_Type"].isin(vehicle))]

# KPI Section
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(df_filtered))
col2.metric("Total Revenue", f"₹{df_filtered['Fare'].sum():,.0f}")
col3.metric("Average Fare", f"₹{df_filtered['Fare'].mean():.2f}")
col4.metric("Average Rating", f"{df_filtered['Customer_Rating'].mean():.2f}")

st.divider()

# Ride Status Chart
st.subheader("Ride Status Distribution")

status_chart = px.pie(
    df_filtered,
    names="Booking_Status",
    title="Ride Status"
)

st.plotly_chart(status_chart, use_container_width=True)

# Vehicle Type Usage
st.subheader("Vehicle Type Usage")

vehicle_chart = px.bar(
    df_filtered.groupby("Vehicle_Type").size().reset_index(name="Rides"),
    x="Vehicle_Type",
    y="Rides",
    color="Vehicle_Type"
)

st.plotly_chart(vehicle_chart, use_container_width=True)

# Revenue by Pickup Location
st.subheader("Revenue by Pickup Location")

location_chart = px.bar(
    df_filtered.groupby("Pickup_Location")["Fare"].sum().reset_index(),
    x="Pickup_Location",
    y="Fare",
    color="Pickup_Location"
)

st.plotly_chart(location_chart, use_container_width=True)

# Ride Trends
st.subheader("Ride Trend")

df_filtered["Date"] = pd.to_datetime(df_filtered["Date"])

trend = df_filtered.groupby("Date").size().reset_index(name="Rides")

trend_chart = px.line(
    trend,
    x="Date",
    y="Rides",
    markers=True
)

st.plotly_chart(trend_chart, use_container_width=True)

# Data Table
st.subheader("Raw Data")

st.dataframe(df_filtered)
