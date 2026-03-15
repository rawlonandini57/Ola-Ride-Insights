import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="OLA Ride Analytics",
    page_icon="🚖",
    layout="wide"
)

# ---------------- LOAD DATA ----------------

@st.cache_data
def load_data():
    df = pd.read_csv("OLA_Ride_Data_Sheet.csv")
    return df

df = load_data()

# ---------------- SIDEBAR ----------------

st.sidebar.title("🚖 OLA Analytics")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Power BI Dashboard",
        "SQL Analysis",
        "Dataset",
        "Project Images"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Data Analytics Project\nSQL | Power BI | Streamlit")

# ---------------- DASHBOARD ----------------

if menu == "Dashboard":

    st.title("📊 OLA Ride Insights Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Bookings", len(df))
    col2.metric("Total Revenue", f"₹{df['Booking_Value'].sum():,.0f}")
    col3.metric("Avg Ride Distance", f"{df['Ride_Distance'].mean():.2f} km")
    col4.metric("Avg Driver Rating", f"{df['Driver_Ratings'].mean():.2f}")

    st.divider()

    # Ride Trend
    st.subheader("📈 Ride Volume Over Time")

    ride_trend = df.groupby("Date")["Booking_ID"].count().reset_index()

    fig = px.line(
        ride_trend,
        x="Date",
        y="Booking_ID",
        markers=True,
        title="Daily Ride Demand"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Booking Status
    st.subheader("📊 Booking Status Breakdown")

    status_data = df["Booking_Status"].value_counts().reset_index()
    status_data.columns = ["Status", "Count"]

    fig2 = px.pie(
        status_data,
        values="Count",
        names="Status"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Vehicle Type
    st.subheader("🚗 Average Ride Distance by Vehicle")

    vehicle_data = df.groupby("Vehicle_Type")["Ride_Distance"].mean().reset_index()

    fig3 = px.bar(
        vehicle_data,
        x="Vehicle_Type",
        y="Ride_Distance",
        color="Vehicle_Type"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # Revenue
    st.subheader("💳 Revenue by Payment Method")

    payment_data = df.groupby("Payment_Method")["Booking_Value"].sum().reset_index()

    fig4 = px.bar(
        payment_data,
        x="Payment_Method",
        y="Booking_Value",
        color="Payment_Method"
    )

    st.plotly_chart(fig4, use_container_width=True)

# ---------------- POWER BI ----------------

elif menu == "Power BI Dashboard":

    st.title("📈 Power BI Dashboard")

    st.write("Power BI analytics created for this project.")

    st.image("images/OLA_POWER_BI-ANSWERS.png", use_container_width=True)

    st.info("Tip: You can embed live Power BI dashboards here.")

# ---------------- SQL ANALYSIS ----------------

elif menu == "SQL Analysis":

    st.title("🗄 SQL Queries & Insights")

    st.image("images/OLA_SQL-ANSWERS.png", use_container_width=True)

    st.subheader("Sample SQL Query")

    st.code("""
SELECT Vehicle_Type,
       AVG(Ride_Distance) AS Avg_Distance
FROM ola_rides
GROUP BY Vehicle_Type;
""", language="sql")

# ---------------- DATASET ----------------

elif menu == "Dataset":

    st.title("📄 Raw Dataset")

    st.dataframe(df)

    st.download_button(
        label="Download Dataset",
        data=df.to_csv(index=False),
        file_name="OLA_Ride_Data.csv",
        mime="text/csv"
    )

# ---------------- IMAGES ----------------

elif menu == "Project Images":

    st.title("🖼 Project Documentation")

    st.image("images/OLA_QUESTIONS.png", caption="Project Questions", use_container_width=True)

    st.image("images/OLA_SQL-ANSWERS.png", caption="SQL Insights", use_container_width=True)

    st.image("images/OLA_POWER_BI-ANSWERS.png", caption="Power BI Dashboard", use_container_width=True)
