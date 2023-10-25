def display_ladder(steps):
    for _ in range(steps):
        print("| |")
        print("***")

def create_ladder():
    try:
        num_steps = int(input("How many steps remain?\n"))
        if num_steps < 1:
            print("Please enter a positive number of steps.")
        else:
            display_ladder(num_steps)
    except ValueError:
        print("Invalid input. Please enter a positive number of steps.")

create_ladder()