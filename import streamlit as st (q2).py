import streamlit as st

# Price reference dictionaries
GIFT_BOX_PRICES = {
    "Standard Box": 25.00,
    "Premium Box": 35.00,
    "Exclusive Box": 45.00
}

GIFT_CARD_PRICES = {
    "Sorry!": 2.00,
    "Happy Birthday!": 3.00,
    "Get Well Soon!": 3.00,
    "Congratulations!": 4.00,
    "Condolence!": 3.00
}

# Page title
st.title("Gift Box Price Calculator")

# Customer Name and Selection Inputs
customer_name = st.text_input("Customer Name")
gift_box = st.selectbox("Gift Box Selection", list(GIFT_BOX_PRICES.keys()))
quantity = st.number_input("Quantity", value=0, step=1)

# Conditional display for Gift Card Option
card_option = st.radio("Gift Card Option", ["No Gift Card", "With Gift Card"])

card_type = None
if card_option == "With Gift Card":
    card_type = st.selectbox("Gift Card Type", list(GIFT_CARD_PRICES.keys()))

# Calculate Price Action
if st.button("Calculate Price"):
    try:
        # Input Validation & Exception Handling
        if not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        box_price = GIFT_BOX_PRICES[gift_box]
        
        # Calculation Logic
        if card_option == "With Gift Card":
            card_price = GIFT_CARD_PRICES[card_type]
            total_price = (box_price * quantity) + card_price
        else:
            card_price = 0.00
            total_price = box_price * quantity

        # Success message
        st.success("Gift box price calculated successfully!")

        # Output Summary
        st.header("Gift Box Summary")
        st.write(f"**Customer Name:** {customer_name}")
        st.write(f"**Gift Box:** {gift_box}")
        st.write(f"**Quantity:** {quantity}")
        st.write(f"**Gift Card:** {card_option}")

        if card_option == "With Gift Card":
            st.write(f"**Gift Card Type:** {card_type}")
            st.write(f"**Gift Card Price:** RM{card_price:.2f}")

        st.write(f"**Total Price:** RM{total_price:.2f}")

    except ValueError as e:
        st.error(f"Input Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")