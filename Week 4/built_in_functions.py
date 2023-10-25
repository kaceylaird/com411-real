print("Program Started!")
character = input("Please enter a standard character: ")
value = ord(character)

if len(character) > 1:
    print("Error! Entry should be a single character!")

else:
    print(f"The ASCII code for {character} is {value}")

print("Program Started!")

print("Please enter an ASCII code: ")

try:
    code = int(input())
    code = abs(code)
except ValueError:
    print("Error: Please enter a valid positive integer.")
    print("Program Ended!")
    exit()

if code in range(32, 127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}.")
else:
    print("Error: The entered code is not within the printable ASCII character range (32-126).")

print("Program Ended!")


