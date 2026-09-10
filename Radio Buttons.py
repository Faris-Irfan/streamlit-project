import streamlit as st

st.title("Radio Button Example")

choice = st.radio("Choose one:", ["Option A", "Option B", "Option C"])

st.write("You selected:", choice)