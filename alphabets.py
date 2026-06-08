char = input("Enter a character: ")

if len(char) == 1 and ((char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')):
    print("The given character is an alphabet.")
else:
    print("The given character is not an alphabet.")