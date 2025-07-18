import streamlit as st
import requests
import os

st.title("Polygon.io Stock Lookup App")

ticker = st.text_input("Enter a stock ticker symbol (e.g., AAPL):")

API_KEY = os.getenv("POLYGON_API_KEY")

if ticker and API_KEY:
    url = f"https://api.polygon.io/v3/reference/tickers/{ticker.upper()}?apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", {})

        if results:
            st.subheader(f"Details for {ticker.upper()}")
            st.write({
                "Name": results.get("name"),
                "Market": results.get("market"),
                "Locale": results.get("locale"),
                "Primary Exchange": results.get("primary_exchange"),
                "Currency": results.get("currency_name"),
                "Active": results.get("active")
            })
        else:
            st.warning("No data found for that ticker.")
    else:
        st.error(f"Error from Polygon.io: {response.status_code}")
elif not API_KEY:
    st.error("Polygon API key not set. Please set the POLYGON_API_KEY environment variable.")

