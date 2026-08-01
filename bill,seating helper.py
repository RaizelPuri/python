def calculate_bill(food, drinks, tax):
    subtotal = food + drinks
    tax_amount = subtotal * tax / 100
    total = subtotal + tax_amount
    return total

def factorial(x):
    ''' THIS IS A RECURSIVE FUNCTION TO FIND THE FACTORIAL OF AN INTEGER'''

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print("===== Bill & Seating Helper =====")
food = float(input("Enter food bill: ₹"))
drinks = float(input("Enter drinks bill: ₹"))
tax = float(input("Enter tax percentage: "))

bill = calculate_bill(food, drinks, tax)
print("\n----- BILL -----")
print("Food Bill   : ₹", food)
print("Drinks Bill : ₹", drinks)
print("Tax         :", tax, "%")
print("Total Bill  : ₹", bill)
print("\nDocstring of factorial function:")
print(factorial.__doc__)
people = int(input("\nEnter the number of people: "))
print("Possible seating arrangements for", people, "people are:", factorial(people))