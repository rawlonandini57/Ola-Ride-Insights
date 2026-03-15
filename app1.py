import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="OLA Ride Insights", layout="wide")

st.title("🚖 OLA Ride Insights Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("OLA_Ride_Data_Sheet.csv")
    return df

df = load_data()

# Create Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dashboard",
    "📈 Power BI",
    "🗄 SQL Queries",
    "📄 Raw Data",
    "🖼 Images"
])

# ---------------- DASHBOARD TAB ----------------
with tab1:

    st.header("Ride Analytics Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Bookings", len(df))
    col2.metric("Total Revenue", f"₹{df['Booking_Value'].sum():,.0f}")
    col3.metric("Average Distance", f"{df['Ride_Distance'].mean():.2f} km")
    col4.metric("Avg Driver Rating", f"{df['Driver_Ratings'].mean():.2f}")

    st.subheader("Ride Volume Over Time")

    ride_trend = df.groupby("Date")["Booking_ID"].count().reset_index()

    fig = px.line(ride_trend, x="Date", y="Booking_ID")
    st.plotly_chart(fig, use_container_width=True)


# ---------------- POWER BI TAB ----------------
with tab2:

    st.header("Power BI Dashboard")

    st.write("Power BI dashboard created for visual analytics.")

    st.image("OLA_POWER_BI-ANSWERS.png", use_container_width=True)


# ---------------- SQL QUERIES TAB ----------------
with tab3:

    st.header("SQL Analysis")

    st.write("SQL queries used to extract insights from the dataset.")

    st.image("OLA_SQL-ANSWERS.png", use_container_width=True)

    st.subheader("Example SQL Query")

    st.code("""
SELECT Vehicle_Type,
       AVG(Ride_Distance) AS Avg_Distance
FROM ola_rides
GROUP BY Vehicle_Type;
""", language="sql")


# ---------------- RAW DATA TAB ----------------
with tab4:

    st.header("Dataset Preview")

    st.dataframe(df)

    st.download_button(
        "Download Dataset",
        df.to_csv(index=False),
        "OLA_Ride_Data.csv",
        "text/csv"
    )


# ---------------- IMAGES TAB ----------------
with tab5:

    st.header("Project Images")

    st.image("OLA_QUESTIONS.png", caption="Project Questions", use_container_width=True)
    st.image("OLA_SQL-ANSWERS.png", caption="SQL Analysis", use_container_width=True)
    st.image("OLA_POWER_BI-ANSWERS.png", caption="Power BI Dashboard", use_container_width=True)
