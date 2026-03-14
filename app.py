import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Page Config
st.set_page_config(page_title="OLA Ride Insights", layout="wide")

st.title("🚕 OLA Ride Insights Dashboard")

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📈 Power BI", "🗄️ SQL Queries", "📋 Raw Data"])

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("OLA_Ride_Data_Sheet.csv")
    return df

df = load_data()

# TAB 1: Dashboard
with tab1:
    st.header("OLA Ride Insights Dashboard")
    
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
    
    if 'Fare' in df_filtered.columns:
        col2.metric("Total Revenue", f"₹{df_filtered['Fare'].sum():,.0f}")
        col3.metric("Average Fare", f"₹{df_filtered['Fare'].mean():.2f}")
    else:
        col2.metric("Total Revenue", "N/A")
        col3.metric("Average Fare", "N/A")
    
    if 'Customer_Rating' in df_filtered.columns:
        col4.metric("Average Rating", f"{df_filtered['Customer_Rating'].mean():.2f}")
    else:
        col4.metric("Average Rating", "N/A")
    
    st.divider()
    
    # Ride Status Chart
    st.subheader("Ride Status Distribution")
    
    if 'Booking_Status' in df_filtered.columns:
        status_chart = px.pie(
            df_filtered,
            names="Booking_Status",
            title="Ride Status"
        )
        st.plotly_chart(status_chart, use_container_width=True)
    
    # Vehicle Type Usage
    st.subheader("Vehicle Type Usage")
    
    vehicle_chart
