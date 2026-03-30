import streamlit as st
import pandas as pd

# Original Stock Portfolio Logic
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 415,
    "NVDA": 875,
}

st.set_page_config(page_title="Stock Portfolio Tracker", page_icon="📈")
st.title("📈 Stock Portfolio Tracker")

# Session state to hold our portfolio
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}

st.sidebar.header("Add to Portfolio")

# Add stock form
with st.sidebar.form(key='add_stock_form', clear_on_submit=True):
    symbol = st.selectbox("Select stock symbol:", options=list(prices.keys()))
    qty_str = st.text_input("Quantity:")
    submit_button = st.form_submit_button(label='Add to Portfolio')
    
    if submit_button:
        if symbol in prices:
            try:
                qty = int(qty_str)
                if qty > 0:
                    if symbol in st.session_state.portfolio:
                        st.session_state.portfolio[symbol] += qty
                    else:
                        st.session_state.portfolio[symbol] = qty
                    st.success(f"Added {qty} shares of {symbol}!")
                else:
                    st.error("Quantity must be greater than 0.")
            except ValueError:
                st.error("Please enter a valid number for quantity.")
        else:
            st.error("Stock not found. Try one of the available stocks!")

# Display logic
st.subheader("Your Current Portfolio")

total_investment = 0
portfolio_data = []

for stock, quantity in st.session_state.portfolio.items():
    current_price = prices[stock]
    value = current_price * quantity
    total_investment += value
    portfolio_data.append({
        "Symbol": stock,
        "Quantity": quantity,
        "Price per Share ($)": current_price,
        "Total Value ($)": value
    })

if portfolio_data:
    df = pd.DataFrame(portfolio_data)
    st.dataframe(df, use_container_width=True)
    st.metric("Total Investment Value", f"${total_investment:,.2f}")
    
    # Simple chart
    st.subheader("Portfolio Breakdown")
    st.bar_chart(df.set_index("Symbol")["Total Value ($)"])
else:
    st.info("Your portfolio is currently empty. Add stocks from the sidebar!")
