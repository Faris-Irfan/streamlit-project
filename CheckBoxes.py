import streamlit as st

st.title("CheckBoxes Example")

agree = st.checkbox("I agree")
disagree = st.checkbox("I Disagree")

if agree:
    st.write("You agreed!")
elif disagree:
    st.write("You disagreed!")