from api.mock import MockDeltaClient

client = MockDeltaClient()

print(client.get_balance())
print(client.get_price())

order = client.place_order("BUY", 0.01)

print(order)

print(client.cancel_order(order["order_id"]))