# 🐍 Binance Futures Testnet Trading Bot

A simplified Python trading bot designed to interact with the **Binance USDT-M Futures Testnet**.  
This project demonstrates the ability to place **Market**, **Limit**, and **Stop-Limit** orders using Binance’s official API.

---

## ✅ Key Features

- 📈 **Place Market Orders** – Instant execution at market price.
- 📉 **Place Limit Orders** – Set specific price conditions for entry/exit.
- 🔐 **Stop-Limit Orders** – Triggered entries with control over price slippage.

---

## 📦 Folder Structure
📦 Project Folder Structure
```graphql
crypto-trading-bot/
├── bot/
│   ├── __init__.py           # Package initializer 
│   ├── core.py               # Main bot logic with all order methods
│   └── logger.py             # Logs API actions and errors
│
├── cli/
│   └── main.py               # Command-line interface (CLI) for user interaction
│
├── config/
│   └── settings.py           # Testnet base URL config
│
├── logs/
│   └── bot.log               # Auto-generated log file for all actions
│
├── requirements.txt          # Python libraries
└── README.md                 # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/adityakumarxd/crypto-trading-bot.git
cd crypto-trading-bot
```

### 2. Install Libraries

```bash
pip install -r requirements.txt
```
### 3. Run the Bot
```bash
python cli/main.py
```


## 💰 Sample Orders
### Market Order:
```makefile
Symbol: BTCUSDT
Side: buy
Quantity: 0.001
```
### Limit Order:
```yaml
Symbol: BTCUSDT
Side: sell
Quantity: 0.002
Limit Price: 101101
```
### Stop-Limit Order:
```vbnet
Symbol: BTCUSDT
Side: buy
Quantity: 0.001
Stop Price (trigger): 111102
Limit Price: 101102
```

