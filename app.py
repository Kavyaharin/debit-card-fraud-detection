import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parent

# Load the saved fraud detection model
model_path = PROJECT_DIR / "models" / "fraud_model.pkl"
fraud_model = joblib.load(model_path)

# Configure the Streamlit page
st.set_page_config(
    page_title="Fraud Watch",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Fraud Watch")
st.write("Debit Card Fraud Detection Demo")


st.subheader("Enter Transaction Details")

# Transaction amount
amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=100.0,
    step=10.0
)

# Payment method
use_chip = st.selectbox(
    "Payment Method",
    ["Swipe", "Chip", "Online"]
)

# Merchant category code
mcc = st.number_input(
    "Merchant Category Code (MCC)",
    min_value=0,
    value=5411,
    step=1
)

# Transaction hour
transaction_hour = st.slider(
    "Transaction Hour",
    min_value=0,
    max_value=23,
    value=14
)

# Run fraud detection when the user clicks the button
if st.button("Check Transaction"):

    # Prepare transaction data in the format expected by the model
    transaction = pd.DataFrame([{
        "amount": amount,
        "use_chip": use_chip,
        "mcc": mcc,
        "transaction_hour": transaction_hour
    }])

    # Predict fraud label and probability
    prediction = fraud_model.predict(transaction)[0]
    fraud_probability = fraud_model.predict_proba(transaction)[0][1]

    # Display prediction result
    st.subheader("Prediction Result")

    if prediction:
        st.error("⚠️ Potential Fraud Detected")
    else:
        st.success("✅ Transaction Appears Genuine")

    st.write(f"Fraud Probability: **{fraud_probability:.2%}**")