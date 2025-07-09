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
crypto-trading-bot/
├── bot/
│ ├── core.py # Trading logic
│ ├── logger.py # Logging configuration
│ └── init.py
├── cli/
│ └── main.py # Command-line interface
├── config/
│ └── settings.py # Testnet URL and configuration
├── logs/
│ └── bot.log # Automatically generated logs
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

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

