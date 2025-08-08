import numpy as np
from scipy.stats import norm

# Calculates the d1 and d2 parameters used in the Black-Scholes formula
def calculate_d1_d2(S, K, T, r, sigma):
    # S: current stock price
    # K: strike price
    # T: time to maturity (in years)
    # r: risk-free interest rate
    # sigma: volatility of the underlying asset
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2

# Calculates the price of a European call option using the Black-Scholes formula
def black_scholes_call(S, K, T, r, sigma):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# Calculates the price of a European put option using the Black-Scholes formula
def black_scholes_put(S, K, T, r, sigma):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price
