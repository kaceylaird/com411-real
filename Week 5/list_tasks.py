def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def run_task1():
    # Call the 'directions' function
    steps = directions()

    for step in steps:
        print(step)

run_task1()

def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path
def generate_movements():
    # This function generates a list of movements.
    # In this example, I'm returning a hardcoded list for demonstration purposes.
    movements = [
        {"direction": "Forward", "steps": 10},
        {"direction": "Left", "steps": 5},
        {"direction": "Right", "steps": 8},
    ]
    return movements

print(" ")
def run_task2():
    # Display a message
    print("Moving...")

    # Call the first function to get the list of movements
    movements = generate_movements()

    # Display the movements in the specified format
    for move in movements:
        direction = move["direction"]
        steps = move["steps"]
        print(f"{direction} for {steps} steps")

# Call the second function to run the task
run_task2()

