# 📈 Quantitative Trading Engine (Pro)
**An automated Python-based algorithmic trading tool built to analyze live cryptocurrency markets and generate data-driven Buy/Sell signals.**

---

### 📖 Project Overview
This project is an intelligent, console-based financial analysis system designed to track dynamic market trends for high-volume assets (like BTC/USDT). It focuses on core quantitative finance principles: **Live API Integration**, **Time-Series Data Analysis**, and **Algorithmic Decision Making**. It allows users to bypass manual chart reading by automatically detecting market momentum and pushing real-time trading insights.

### 🛠️ Tech Stack & Skills
* **Language:** Python 3
* **Libraries:** `requests`, `pandas`
* **Data Science & Analytics:** Time-series manipulation, rolling averages, and structured DataFrame filtering using Pandas.
* **API Integration:** Handling real-time REST API calls and parsing unstructured JSON payloads into clean datasets.

### 🚀 Key Technical Features
* **Live Market Data Fetching:** Directly connects to the Binance Public API to securely pull the latest 90-day daily candlestick data without requiring paid API keys.
* **Algorithmic Trend Detection:** Implements a mathematical trading strategy known as the **Simple Moving Average (SMA) Crossover**. It tracks short-term (9-day) vs long-term (21-day) momentum to identify breakouts and trend reversals.
* **Robust Data Transformation:** Engineered with Pandas to clean raw JSON data, enforce strict data types (floats), and calculate dynamic rolling averages instantly.
* **Dynamic Console Dashboard:** Automatically converts real-time USD prices to INR (₹) and formats the output into a premium, human-readable terminal dashboard with clear, logic-backed trading signals.

---

### 💻 Output Dashboard
The script features a clean, formatted terminal dashboard that converts live prices dynamically. Here is an example of the real-time execution:

    ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
     🚀 QUANTITATIVE TRADING ENGINE (PRO) 🚀
    ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

    [*] Initializing system parameters...
    [*] Fetching real-time market data via Binance API...

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     📊 LIVE MARKET DASHBOARD (INR)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     💰 Current Price    : ₹ 6,306,891.94
     📈 9-Day Average (S) : ₹ 6,446,144.80
     📉 21-Day Average (L): ₹ 6,605,714.90
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

     🎯 ALGORITHMIC SIGNAL:
     🔴 STATUS : [ SELL / WAIT ]
     📝 REASON : Market is in a DOWNTREND.
                 (Short-term momentum < Long-term momentum)

    ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

---

### 🛠️ How to Run

1. **Clone the Repository:**
    git clone https://github.com/NishantScripts/Quantitative-Trading-Engine-Pro.git

2. **Install Dependencies:**
    Ensure you have Python installed, then run:
    pip install requests pandas

3. **Execute:**
    Run the script using your terminal or Python IDE:
    python algo_main.py

4. **View Output:**
    The script will instantly fetch live data and display the current market trend (Uptrend/Downtrend) alongside a generated signal (BUY or SELL/WAIT).

---
*Developed by [NishantScripts](https://github.com/NishantScripts)*
