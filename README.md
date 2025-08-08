# Black-Scholes Option Pricing App  

An interactive web application for calculating **Call and Put option prices** using the **Black-Scholes model**, featuring **heatmap visualizations** of results.  
Built in **Python** with [Streamlit](https://streamlit.io/), designed for visual analysis and educational purposes.  

---
## 📌 Features

- **Real-time calculation** of Call and Put option prices using the Black-Scholes model
- **Interactive interface** to adjust:
  - Spot Price (current asset price)
  - Strike Price
  - Time to expiration
  - Volatility
  - Risk-free rate
- **Dynamic heatmaps** showing how option prices vary with changes in:
  - Spot Price
  - Volatility
- Customizable axis ranges for heatmaps via sidebar controls

---
## 📚 Theoretical Foundations

### What is an Option?
An option is a contract that gives the **right**, but not the obligation, to buy (**Call**) or sell (**Put**) an underlying asset at a fixed price (Strike Price) on a future date.

### Black-Scholes Model
The Black-Scholes model values European options using:
- **Spot Price (S)**
- **Strike Price (K)**
- **Time to expiration (T)**
- **Volatility (σ)**
- **Risk-free rate (r)**

Equations:
\[
d_1 = \frac{\ln(S/K) + (r + \frac{σ^2}{2})T}{σ \sqrt{T}}, \quad d_2 = d_1 - σ \sqrt{T}
\]
\[
C = S N(d_1) - K e^{-rT} N(d_2)
\]
\[
P = K e^{-rT} N(-d_2) - S N(-d_1)
\]

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your_username/black-scholes-app.git
cd black-scholes-app
```
### 2️⃣ Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```
### 3️⃣ Run the application
```bash
streamlit run app.py
```

## 🖥️ Application Interface
![Black-Scholes Option Pricing App](images/app_screenshot.png)
*Interactive interface showing real-time option pricing and volatility heatmap*

---

## ✨ Key Features

### 📊 Dynamic Pricing Visualization
- Real-time updates of option prices as parameters change
- Dual heatmap display showing price sensitivity to:
  - Underlying asset price (Spot Price)
  - Market volatility


