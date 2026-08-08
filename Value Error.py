try:
    number = int(input("ENTER A NUMBER: "))
    print("THE NUMBER ENTERED IS", number)

except ValueError as ex:
    print("EXCEPTION: ",ex)