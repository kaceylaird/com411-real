mountains = int(input("How many mountains do you want to display? "))
print("Displaying...")
for count in range(mountains):
    print("       __")
    print("      /  \_")
    print("     /^    \ ")
    print("    /  ^    \_ ")
    print("  _/ ^ ^     ^\ ")
    print(" /  ^     ^    \ ")

stepsAway = int(input("How many steps away are we from the target? "))
stepCount = 1

for count in range(stepsAway):
    stepsAway = stepsAway - 1
    print(f"{stepsAway} steps away.. ")

print("Target Achieved!")

required_brightness = int(input("What level of brightness is required? "))

# Check if the input is even
if required_brightness % 2 != 0:
    print("Please enter an even number for brightness.")
else:
    # Generate a range of even numbers between 2 and the user's input
    brightness_range = range(2, required_brightness + 1, 2)

    # Use a for loop to display asterisk symbols to represent the current light level
    for brightness in brightness_range:
        # Calculate the number of asterisks to display
        num_asterisks = brightness // 2
        print("Brightness level:", brightness)
        print("*" * num_asterisks)
