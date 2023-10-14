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