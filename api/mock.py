import random
from datetime import datetime


class MockDeltaClient:

    def get_balance(self):
        return {
            "currency": "USDT",
            "balance": 100000
        }

    def get_price(self):
        return {
            "symbol": "BTCUSD",
            "price": round(random.uniform(105000, 110000), 2),
            "time": datetime.now()
        }

    def place_order(self, side, quantity):

        return {
            "status": "success",
            "order_id": random.randint(100000, 999999),
            "side": side,
            "quantity": quantity
        }

    def cancel_order(self, order_id):

        return {
            "status": "cancelled",
            "order_id": order_id
        }