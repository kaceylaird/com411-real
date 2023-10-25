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


# Function to display the word in a box
def display_in_box(word):
    box_width = len(word) + 4
    print("*" * box_width)
    print(f"* {word} *")
    print("*" * box_width)


# Function to display the word in lower-case
def display_lower_case(word):
    print(word.lower())


# Function to display the word in upper-case
def display_upper_case(word):
    print(word.upper())


# Function to display the word and its mirrored version
def display_mirrored(word):
    mirrored_word = word[::-1]
    print(f"{word} | {mirrored_word}")


# Function to repeat the word with alternating upper-case and lower-case
def display_repeated(word, times):
    repeated_word = ""
    for i in range(times):
        if i % 2 == 0:
            repeated_word += word.lower()
        else:
            repeated_word += word.upper()
    print(repeated_word)


# Function to run the program
def run():
    word = input("Enter a word: ")
    option = int(input(
        "Choose an option:\n1) Display in a Box\n2) Display Lower-case\n3) Display Upper-case\n4) Display Mirrored\n5) Repeat\n"))

    if option == 1:
        display_in_box(word)
    elif option == 2:
        display_lower_case(word)
    elif option == 3:
        display_upper_case(word)
    elif option == 4:
        display_mirrored(word)
    elif option == 5:
        times = int(input("Enter how many times to display: "))
        display_repeated(word, times)
    else:
        print("Invalid option. Please choose a valid option (1-5).")


# Run the program
run()

