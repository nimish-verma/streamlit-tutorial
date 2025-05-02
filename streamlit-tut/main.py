# def main():
#     print("Hello from streamlit-tut!")


# if __name__ == "__main__":
#     main()

import streamlit as st
st.title("basic ass app")
st.subheader("made w streamlit")
st.text("welcome to the app thingy, wussup homie")
st.write("choose your coffee type: ")

# makes a dropdown
coffee = st.selectbox("your favourite coffee: ", ["cappucino", "latte", "frappucino"])
st.write(f"you chose: {coffee}, excellent choice")

st.success("your coffee has been brewed.")
