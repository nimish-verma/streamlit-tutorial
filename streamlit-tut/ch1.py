# def main():
#     print("Hello from streamlit-tut!")


# if __name__ == "__main__":
#     main()

# import streamlit as st
# st.title("basic ass app")
# st.subheader("made w streamlit")
# st.text("welcome to the app thingy, wussup homie")
# st.write("choose your coffee type: ")
# coffee = st.selectbox("your favourite coffee: ", ["cappucino", "latte", "frappucino"])
# st.write(f"you chose: {coffee}, excellent choice")
# st.success("your coffee has been brewed.")

import streamlit as st
st.title("prog lang picker type shit")
st.subheader("making a subheader to ensure working type shit")
st.text("wussup homie, pick a language")
st.write("choose some shit, yo ")
prog = st.selectbox("pick yo shit: ", ["c", "python", "js"])
st.write(f"pulling out real quick, thats yo shit {prog}, pull up babygirl")
st.success("making sure shit works as intended.")