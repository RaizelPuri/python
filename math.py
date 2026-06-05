import math
# Input from user
num = float(input("Enter a number: "))

# Check for negative numbers
if num < 0:
    print("Square root of a negative number is not a real number.")
else:
    result = math.sqrt(num)
    print(f"The square root of {num} is {result}")

