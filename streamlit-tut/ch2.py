import streamlit as st
st.title("coffee maker app")
if st.button("wanna make coffee, nigga ?"):
    st.success("your coffee ready, nigga")

add_sugar = st.checkbox("add sugar ??")
if add_sugar:
    st.write("sugar added to your coffee, you fine?")

coffee_type = st.radio("pick ur coffee base", ["milk", "water", "coffee", "honey", "sugar", "almond milk"])
st.write(f"selected base: {coffee_type}")

flavour = st.selectbox("choose flavour: ", ["wine", "cold hearted", "beer type"])
st.write(f"selected flavour: {flavour}")

sugar_level = st.slider("sugar level: ", 0,5,2)
st.write(f"this is the sugar level {sugar_level}")