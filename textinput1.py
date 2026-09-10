import streamlit as st

st.title("Text Input Example")

name = st.text_input("Enter your name:")

if name:
    st.write("Hello,", name)