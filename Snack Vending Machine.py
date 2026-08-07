def calculate_change(paid,price):
    change=paid-price
    return change

snack_price=25
print("====== SNACK VENDING MACHINE ======")
print(f" THIS SNACK COSTS {snack_price} UNITS.")
print('ACCEPTED COINS: 1, 5, 10, 25 \n')

total_inserted=0
coins_inserted=0

while True:
    coin = int(input("INSERT A COIN (1, 5, 10, 25):"))
    if coin !=1 and coin !=5 and coin !=10 and coin !=25:
        print("INVALID COIN, TRY AGAIN!!\n")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"INSERTED {coin}, TOTAL SO FAR: {total_inserted}\n")
    if total_inserted >= snack_price:
        print("enough money inserted!\n")
        break

change_due= calculate_change(total_inserted,snack_price)

print("DISPENSING YOUR SNACK.....")

if change_due==0:
        pass
else:
        print(f"HERE IS YOUR CHANGE: {change_due}UNITS")

print("\n ======= PURCHASE SUMMARY =======")
print("SNACK PRICE: ",snack_price)
print("COINS INSERTED:",coins_inserted)
print("TOTAL PAID:",total_inserted)
print("============================================")
print("THANKS FOR YOUR PURCHASE!!")