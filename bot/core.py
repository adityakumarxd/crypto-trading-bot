from binance.client import Client
from binance.enums import *
from bot.logger import logger
from config.settings import BINANCE_TESTNET_URL



class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = BINANCE_TESTNET_URL

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logger.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logger.error(f"Market order error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logger.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logger.error(f"Limit order error: {e}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol.upper(),
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type='STOP',
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logger.info(f"Stop-Limit order placed: {order}")
            return order
        except Exception as e:
            logger.error(f"Stop-Limit order error: {e}")
            raise
