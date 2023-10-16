for number in range(0, 10, 1):
    print(f"{number} |", end="")
print("")
columns = int(input("How many columns would you like? "))
rows = int(input("How many rows would you like? "))

for count in range(0, rows):
    for number in range(0, columns, 1):
        print(" :-) ", end="")
    print()

sequence = input("Enter a sequence of characters consisting of dashes and two markers (e.g., 'X----X'): ")
marker = input("Enter the marker character (e.g., 'X'): ")

dash_count = 0

inside_markers = False

for char in sequence:
    if char == marker:
        if inside_markers:
            inside_markers = False
        else:
            inside_markers = True
    elif inside_markers and char == '-':
        dash_count += 1

print("Total number of characters between the markers:", dash_count)
