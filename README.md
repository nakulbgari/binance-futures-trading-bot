# Binance Futures Testnet Trading Bot

A simplified Python-based trading bot that places MARKET and LIMIT orders on **Binance Futures Testnet (USDT-M)**.

This project demonstrates:
- Clean and modular code structure
- Separation of concerns (Client, Orders, Validators, CLI)
- Proper logging of API responses and errors
- Input validation via CLI
- Exception handling

---

## 📌 Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- CLI-based execution using argparse
- Structured logging to file
- Error handling for invalid input and API errors

---

## 🏗 Project Structure
binance-futures-trading-bot/
│
├── bot/
│ ├── init.py
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── logs/
│ └── market_and_limit_orders.log
│
├── cli.py
├── README.md
├── requirements.txt
└── .gitignore


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository


git clone https://github.com/nakulbgari/binance-futures-trading-bot.git
cd binance-futures-trading-bot
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create .env File

Create a .env file in the root directory:

API_KEY=your_futures_testnet_api_key
API_SECRET=your_futures_testnet_secret_key

⚠️ Use Binance Futures Testnet API keys
⚠️ Do NOT use real Binance production API keys

Testnet Base URL used:

https://testnet.binancefuture.com
🚀 Usage Examples
▶️ Place MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
▶️ Place LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000
📝 Logging

All order responses and errors are logged in:

logs/market_and_limit_orders.log

Logging includes:

Order ID

Order type

Order side

Status

API errors (if any)

🛡 Error Handling

The application handles:

Invalid order side

Invalid order type

Missing price for LIMIT orders

API authentication errors

Network/API exceptions

🧠 Assumptions

User provides a valid trading symbol (e.g., BTCUSDT)

Futures Testnet account is active

API keys have trading permissions enabled

📦 Requirements

Python 3.x

python-binance

python-dotenv

Install using:

pip install -r requirements.txt

📌 Author:-  Nakul
