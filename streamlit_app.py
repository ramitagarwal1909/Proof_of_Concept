import streamlit as st

st.title("Polygon.io Stock Lookup App")

ticker = st.text_input("Enter a stock ticker symbol (e.g., AAPL):")

if ticker:
    st.write(f"You entered: {ticker}")
