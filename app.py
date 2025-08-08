import streamlit as st
from bs_pricing import black_scholes_call, black_scholes_put
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import base64
# Set Streamlit page layout to wide
st.set_page_config(layout="wide")
st.write("# Black-Scholes Option Pricing Calculator")

# Dynamically generate absolute path for the image
img_path = Path(__file__).parent / "images" / "icon.png"
img_path = str(img_path.resolve())

# Check if the local image file exists
p = Path(img_path)
if not p.exists():
    st.sidebar.error("icon.png not found in the current directory.")
else:
    # Encode the image in base64 for embedding in HTML
    b64 = base64.b64encode(p.read_bytes()).decode()
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    data_uri = f"data:{mime};base64,{b64}"

    # Display the app icon and title in the sidebar
    st.sidebar.markdown(
        f"""
        <div style="display:flex; align-items:center;">
            <img src="{data_uri}" width="40" style="margin-right:10px;">
            <h1 style="margin:0; font-size:22px;">Black-Scholes Model</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Display the "Created by" section in the sidebar
    st.sidebar.markdown(
        "<span style='background-color: #163020; color: #00FF00; "
        "padding: 2px 8px; border-radius: 5px; font-family: monospace; font-size:12px;'>"
        "Created by:"
        "</span>",
        unsafe_allow_html=True,
    )

    # Display LinkedIn profile with icon and name
    st.sidebar.markdown(
        """
        <div style="display:flex; align-items:center; margin-top:1px;">
            <a href="https://www.linkedin.com/in/carlos-tornez-859a17144" target="_blank"
               style="display:inline-block; margin-right:8px;">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20">
            </a>
            <span style='background-color: #1f1f1f; color: white;
                         padding: 2px 8px; border-radius: 5px; font-family: monospace;font-size:12px;'>
                Tornez Membrila, Jose Carlos
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

def user_input():
    st.sidebar.divider()
    # User inputs for Black-Scholes parameters
    S = st.sidebar.number_input("Current Stock Price", min_value=0.0, value=100.0)
    K = st.sidebar.number_input("Strike Price", min_value=0.0, value=100.0)
    T = st.sidebar.number_input("Time to Expiration (Years)", min_value=0.0, value=1.0)
    r = st.sidebar.number_input("Risk-Free Interest Rate (%)", min_value=0.0, value=5.0) / 100
    sigma = st.sidebar.number_input("Volatility (%)", min_value=0.0, value=20.0) / 100
    # Store user inputs in a dictionary
    dic = {
        "Current Asset Price (S)": [S],
        "Strike Price (K)": [K],
        "Time to Expiration (T)": [T],
        "Risk-Free Interest Rate (r)": [r],
        "Volatility (σ)": [sigma]
    }
    return dic

def heatmap_parameters(volatility, spot_price):
    volatility_lower_bound = volatility-volatility*0.5
    volatility_upper_bound = volatility+volatility*0.5
    spot_price_lower_bound = spot_price-spot_price*0.5
    spot_price_upper_bound = spot_price+spot_price*0.5
    st.sidebar.divider()
    # Section for heatmap parameter selection
    st.sidebar.button("### Heatmap Parameters")
    min_spot_price = st.sidebar.number_input("Min Spot Price", min_value=0.0, value=spot_price_lower_bound, key="min_spot_price")
    max_spot_price = st.sidebar.number_input("Max Spot Price", min_value=0.1, value=spot_price_upper_bound, key="max_spot_price")
    spot_prices_range = [min_spot_price, max_spot_price]
    # Slider for volatility range
    volatilities_range = np.array(st.sidebar.slider("Volatilities (%)", volatility_lower_bound*100, volatility_upper_bound*100, (volatility_lower_bound*100, volatility_upper_bound*100), step=0.01, key="volatilities_range"))/100
    return spot_prices_range, volatilities_range

# Get user input and heatmap parameters
user_input_information = user_input()
S, K, T, r, sigma = user_input_information["Current Asset Price (S)"][0], user_input_information["Strike Price (K)"][0], user_input_information["Time to Expiration (T)"][0], user_input_information["Risk-Free Interest Rate (r)"][0], user_input_information["Volatility (σ)"][0]
user_input_information_df = pd.DataFrame(user_input_information)
spot_prices_range, volatilities_range = heatmap_parameters(sigma, S)

# Display user input parameters as a dataframe
st.dataframe(user_input_information_df, use_container_width=True)

# Common configuration for info boxes
wch_colour_box1 = (144, 238, 144)  # green background for put value
wch_colour_box2 = (250, 218, 217)  # light red background for call value
wch_colour_font = (0, 0, 0)        # black font color
fontsize = 14

# Create two columns for displaying option values
col1, col2 = st.columns(2)

# First box: Put value
with col1:
    # Display the calculated put option value
    htmlstr1 = f"""<p style="background-color:rgb({wch_colour_box1[0]},{wch_colour_box1[1]},{wch_colour_box1[2]},0.75);
                    color: rgb({wch_colour_font[0]},{wch_colour_font[1]},{wch_colour_font[2]});
                    font-size: {fontsize}px;
                    border-radius: 7px;
                    padding: 10px 12px;
                    line-height:10px;
                    margin: 0;
                    height: 60px;
                    text-align: center;">
                    <i class></i> PUT value
                    <br>
                    <br>
                    <br>
                    <span style='font-size: 22px;'> <b>${black_scholes_put(S, K, T, r, sigma):.2f}</b></span>
                    </p>"""
    st.markdown(htmlstr1, unsafe_allow_html=True)

# Second box: Call value
with col2:
    # Display the calculated call option value
    htmlstr2 = f"""<p style="background-color:rgb({wch_colour_box2[0]},{wch_colour_box2[1]},{wch_colour_box2[2]},0.75);
                    color: rgb({wch_colour_font[0]},{wch_colour_font[1]},{wch_colour_font[2]});
                    font-size: {fontsize}px;
                    border-radius: 7px;
                    padding: 10px 12px;
                    line-height:10px;
                    margin: 0;
                    height: 60px;
                    text-align: center;">
                    <i class></i> CALL Value
                    <br>
                    <br>
                    <br>
                    <span style='font-size: 22px; font-weight: bald'> <b>${black_scholes_call(S, K, T, r, sigma):.2f}</b></span>
                    </p>"""
    st.markdown(htmlstr2, unsafe_allow_html=True)

# Add FontAwesome CSS for icons (only once)
st.markdown('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" crossorigin="anonymous">', 
            unsafe_allow_html=True)

st.write("## Options Price - Interactive Heatmap")

col3, = st.columns(1)

# Info box for heatmap explanation
with col3:
    # Explain the purpose of the heatmap to the user
    htmlstr1 = f"""<p style="background-color:rgb(4,11,59,0.45);
                    color: rgb(252,252,252);
                    font-size: {fontsize}px;
                    border-radius: 7px;
                    padding: 10px 12px;
                    line-height:10px;
                    margin: 0;
                    height: 40px;
                    text-align: left;">
                    <i class></i> Explore how option prices fluctuate with varying 'Spot Prices' and 'Volatility' levels using an interactive heatmap, while keeping constant the 'Strike Price', 'Time to Expiration', and the 'Risk-Free Interest Rate'.
                    <br>
                    <br>
                    <br>
                    </p>"""
    st.markdown(htmlstr1, unsafe_allow_html=True)

col4, col5 = st.columns(2)

# Call option price heatmap
with col4:
    st.write("### Call Option Price Heatmap")
    # Generate spot price and volatility ranges for the heatmap
    spot_prices = np.linspace(spot_prices_range[0], spot_prices_range[1], 10)
    volatilities = np.linspace(volatilities_range[0], volatilities_range[1], 10)
    # Create meshgrid for spot prices and volatilities
    S_grid, sigma_grid = np.meshgrid(spot_prices, volatilities)
    # Calculate call option prices for the grid
    call_price = black_scholes_call(S_grid, K, T, r, sigma_grid)
    plt.figure(figsize=(10, 8))
    # Plot heatmap for call option prices
    sns.heatmap(np.round(call_price, 2), xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities*100, 2), cmap='magma', annot=True, cbar_kws={'label': 'Call Price'})
    plt.xlabel("Spot Price")
    plt.ylabel("Volatility(%)")
    st.pyplot(plt)

# Put option price heatmap
with col5:
    st.write("### Put Option Price Heatmap")
    # Generate spot price and volatility ranges for the heatmap
    spot_prices = np.linspace(spot_prices_range[0], spot_prices_range[1], 10)
    volatilities = np.linspace(volatilities_range[0], volatilities_range[1], 10)
    # Create meshgrid for spot prices and volatilities
    S_grid, sigma_grid = np.meshgrid(spot_prices, volatilities)
    # Calculate put option prices for the grid
    put_price = black_scholes_put(S_grid, K, T, r, sigma_grid)
    plt.figure(figsize=(10, 8))
    # Plot heatmap for put option prices
    sns.heatmap(np.round(put_price, 2), xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities*100, 2), cmap='magma', annot=True, cbar_kws={'label': 'Put Price'})
    plt.xlabel("Spot Price")
    plt.ylabel("Volatility(%)")
    st.pyplot(plt)

