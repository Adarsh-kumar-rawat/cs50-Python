PRICE = 50
ACCEPTED_COINS = [25, 10, 5]
total = 0

while total < PRICE:
    print(f"Amount Due: {PRICE - total}")
    coin = int(input("Insert Coin: "))
    if coin in ACCEPTED_COINS:
        total += coin

print(f"Change Owed: {total - PRICE}")
