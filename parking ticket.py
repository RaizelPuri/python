ticket_price = 25

def calculate_change(total_paid, ticket_price):
    return total_paid - ticket_price

print("====== PARKING TICKET PAYMENT HELPER ======")
print(f" THIS PARKING TICKET COSTS {ticket_price} UNITS.")
print("ACCEPTED COINS: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("INSERT A COIN (1, 5, 10, 25): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("INVALID COIN, TRY AGAIN!!\n")
        continue

    total_inserted += coin
    coins_inserted += 1

    print(f"INSERTED {coin}, TOTAL SO FAR: {total_inserted}\n")

    if total_inserted >= ticket_price:
        print("ENOUGH MONEY INSERTED!\n")
        break

change_due = calculate_change(total_inserted, ticket_price)

print("PROCESSING YOUR PARKING TICKET.....")

if change_due == 0:
    pass
else:
    print(f"HERE IS YOUR CHANGE: {change_due} UNITS")

print("\n======= PAYMENT SUMMARY =======")
print("TICKET PRICE:", ticket_price)
print("COINS INSERTED:", coins_inserted)
print("TOTAL PAID:", total_inserted)
print("CHANGE:", change_due)
print("================================")
print("THANKS FOR YOUR PAYMENT!!")