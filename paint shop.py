def greet_customer():
    print("Welcome to the Paint Shop!!")
    print("We Have All Shades Of Colours.")

greet_customer()

price_per_cup = float(input("Enter the price per colour tube in dollars: "))
cups_sold = int(input("Enter the number of tubes sold: "))
def calculate_total(price,cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total= round(total_cost,2)
print("TOTAL COST: ", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer:  "))

def calculate_change(paid,total):
    change = paid-total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups>=5:
        return "WOW,  big order!!  THANKS so much for your support!"
    else:
        return "THANKS for stopping by the shop!!!"

closing_message = thank_you_message(cups_sold)

print("")
print("===== COLOUR SHOP =====")
print("Price Per Tube: ", price_per_cup)
print("Tubes Sold: ", cups_sold)
print("Total Cost: ",rounded_total)
print("Amount Paid: ",amount_paid)
print("Change Due: ",rounded_change)
print(closing_message)
print("=======================================")