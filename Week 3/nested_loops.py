for number in range(0, 10, 1):
    print(f"{number} |", end="")
print("")
columns = int(input("How many columns would you like? "))
rows = int(input("How many rows would you like? "))

for count in range(0, rows):
    for number in range(0, columns, 1):
        print(" :-) ", end="")
    print()