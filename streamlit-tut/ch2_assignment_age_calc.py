import streamlit as st

st.title("Age Calculator")
st.subheader("Welcome to the age calculator, wussup, you good fam ?????")

today_date = st.date_input(value="today", max_value="today", label="today")
st.write(f"so today is {today_date}, nigga you good")

dob = st.date_input("enter your dob, nigga: ")
st.write(f"your entered date is: {dob}")
age = today_date - dob
st.write(f"thats your age, homie: {age}")


