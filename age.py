print("Age Category Checker")

age = int(input("Enter your age: "))

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teen"
else:
    category = "Adult"

print("Your category is:", category)