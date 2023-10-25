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

# Function to calculate the total weight
def sum_weights(character_weight, inventory_weight):
    return character_weight + inventory_weight

# Function to calculate the average weight
def calc_avg_weight(character_weight, inventory_weight):
    total_weight = sum_weights(character_weight, inventory_weight)
    return total_weight / 2

# Function to run the program
def run():
    character_weight = float(input("What is the weight of the person?\n"))
    inventory_weight = float(input("What is the weight of their inventory?\n"))

    calculation_choice = input("What would you like to calculate (sum or average)?\n")

    if calculation_choice == "sum":
        total_weight = sum_weights(character_weight, inventory_weight)
        print(f"The sum of weights is {total_weight}.")
    elif calculation_choice == "average":
        average_weight = calc_avg_weight(character_weight, inventory_weight)
        print(f"The average weight is {average_weight}.")
    else:
        print("Invalid choice. Please enter either 'sum' or 'average'.")

run()
