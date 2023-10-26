def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def run_task1():
    # Call the 'directions' function
    steps = directions()

    for step in steps:
        print(step)

run_task1()

