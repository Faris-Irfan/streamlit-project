import streamlit as st

st.title("Button Example")

matricNum = st.text_input("Your Matric Number:")
if st.button("Submit"):
    st.success(f"Your Matric Number is {matricNum}")