import streamlit as st

st.title("🗄 SQL Analysis")

st.image("images/OLA_SQL-ANSWERS.png")

st.code("""
SELECT Vehicle_Type,
AVG(Ride_Distance)
FROM ola_rides
GROUP BY Vehicle_Type;
""", language="sql")
