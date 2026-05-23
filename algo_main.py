import requests
import pandas as pd

# USD to INR Conversion Rate (Approximate exchange rate)
USD_TO_INR = 83.50

print("\n" + "★"*55)
print(" 🚀 QUANTITATIVE TRADING ENGINE (PRO) 🚀")
print("★"*55 + "\n")

print("[*] Initializing system parameters...")
print("[*] Fetching real-time market data via Binance API...\n")

# 1. Fetching live daily candle data from API
url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=90"
response = requests.get(url)
data = response.json()

# 2. Converting raw JSON data into a structured Pandas DataFrame
df = pd.DataFrame(data, columns=[
    'Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 
    'Close_time', 'Quote_asset_volume', 'Trades', 
    'Taker_buy_base', 'Taker_buy_quote', 'Ignore'
])

# Ensure Close prices are floats for mathematical calculations
df['Close'] = df['Close'].astype(float)

# --- QUANTITATIVE ANALYSIS: MOVING AVERAGES ---

# 3. Calculating the 9-day and 21-day Simple Moving Averages (Rolling Averages)
df['SMA_9'] = df['Close'].rolling(window=9).mean()
df['SMA_21'] = df['Close'].rolling(window=21).mean()

# 4. Extracting the latest live status and converting to INR (Rupees)
current_close_usd = df['Close'].iloc[-1]
current_close_inr = current_close_usd * USD_TO_INR
current_sma9_inr = df['SMA_9'].iloc[-1] * USD_TO_INR
current_sma21_inr = df['SMA_21'].iloc[-1] * USD_TO_INR

# --- BEAUTIFIED OUTPUT DASHBOARD ---
print("━"*55)
print(" 📊 LIVE MARKET DASHBOARD (INR)")
print("━"*55)

# Use :,.2f for professional comma formatting and 2 decimal places
print(f" 💰 Current Price    : ₹ {current_close_inr:,.2f}")
print(f" 📈 9-Day Average (S) : ₹ {current_sma9_inr:,.2f}")
print(f" 📉 21-Day Average (L): ₹ {current_sma21_inr:,.2f}")
print("━"*55 + "\n")

# --- TRADING SIGNAL LOGIC ---
print(" 🎯 ALGORITHMIC SIGNAL:")
if current_sma9_inr > current_sma21_inr:
    print(" 🟢 STATUS : [ STRONG BUY ]")
    print(" 📝 REASON : Market is in a clear UPTREND.")
    print("             (Short-term momentum > Long-term momentum)")
else:
    print(" 🔴 STATUS : [ SELL / WAIT ]")
    print(" 📝 REASON : Market is in a DOWNTREND.")
    print("             (Short-term momentum < Long-term momentum)")

print("\n" + "★"*55 + "\n")
