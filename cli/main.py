import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bot.core import BasicBot

def run_cli():
    print("\n📈 Welcome to Binance Futures Trading Bot")

    api_key = input("🔑 Enter your API Key: ")
    api_secret = input("🔐 Enter your API Secret: ")
    bot = BasicBot(api_key, api_secret)

    while True:
        print("\n1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Place Stop-Limit Order")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            symbol = input("Symbol (e.g. BTCUSDT): ").upper()
            side = input("Side (buy/sell): ").lower()
            qty = float(input("Quantity: "))
            try:
                result = bot.place_market_order(symbol, side, qty)
                print("✅ Market Order Placed:", result)
            except Exception as e:
                print("❌ Failed:", str(e))

        elif choice == '2':
            symbol = input("Symbol: ").upper()
            side = input("Side (buy/sell): ").lower()
            qty = float(input("Quantity: "))
            price = input("Limit Price: ")
            try:
                result = bot.place_limit_order(symbol, side, qty, price)
                print("✅ Limit Order Placed:", result)
            except Exception as e:
                print("❌ Failed:", str(e))

        elif choice == '3':
            symbol = input("Symbol: ").upper()
            side = input("Side (buy/sell): ").lower()
            qty = float(input("Quantity: "))
            stop_price = input("Stop Price (trigger): ")
            limit_price = input("Limit Price: ")
            try:
                result = bot.place_stop_limit_order(symbol, side, qty, stop_price, limit_price)
                print("✅ Stop-Limit Order Placed:", result)
            except Exception as e:
                print("❌ Failed:", str(e))

        elif choice == '4':
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_cli()
