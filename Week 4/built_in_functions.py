print("Program Started!")
character = input("Please enter a standard character: ")
value = ord(character)

if len(character) > 1:
    print("Error! Entry should be a single character!")

else:
    print(f"The ASCII code for {character} is {value}")