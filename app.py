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

# IMPORTANT: Display all column names to identify the issue
st.write("**Available Columns in CSV:**")
st.write(df.columns.tolist())
st.write("**Data shape:**", df.shape)
st.write("**First few rows:**")
st.write(df.head())

# Stop here to see the columns
st.stop()
