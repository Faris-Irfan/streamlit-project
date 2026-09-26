import streamlit as st

# Page title
st.title("Restaurant Table Booking System")

# Form inputs using required Streamlit widgets
customer_name = st.text_input("Customer Name")
num_guests = st.number_input("Number of Guests", value=0, step=1)
table_type = st.selectbox("Table Type", ["Standard Table", "Family Table", "Private Table"])
dining_time = st.radio("Dining Time", ["12:00 PM", "2:00 PM", "7:00 PM", "8:00 PM"])

st.write("Special Request:")
req_celebration = st.checkbox("Celebration")
req_baby_chair = st.checkbox("Baby Chair")
req_window_seat = st.checkbox("Window Seat")

# Reserve Table Action
if st.button("Reserve Table"):
    try:
        # Input Validation & Exception Handling
        if not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if num_guests <= 0:
            raise ValueError("Number of guests must be greater than 0.")

        # Success message
        st.success("Table reserved successfully!")

        # Booking Information Output
        st.header("Booking Information")
        st.write(f"**Customer Name:** {customer_name}")
        st.write(f"**Number of Guests:** {num_guests}")
        st.write(f"**Table Type:** {table_type}")
        st.write(f"**Dining Time:** {dining_time}")

        # Display Special Requests if selected
        st.write("**Special Request:**")
        requests = []
        if req_celebration:
            requests.append("Celebration")
        if req_baby_chair:
            requests.append("Baby Chair")
        if req_window_seat:
            requests.append("Window Seat")

        if requests:
            for req in requests:
                st.write(f"• {req}")
        else:
            st.write("• None")

        st.info("Thank you for booking with us! We look forward to serving you.")

    except ValueError as e:
        st.error(f"Input Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")