def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def run():
    print(pattern())


run()


def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()


def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)
    print()


def display_pairs(data):
    print("Pairs:")
    for key, value in data:
        print(f"{key}: {value}")
    print()


def run():
    data = pattern()
    print(f"Dictionary:\n{data}")

    display_keys(data)
    display_values(data)
    display_pairs(data)


run()


def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run_task3():
    print("Analysing patterns...")
    patterns = {
        "short sequence": short_pattern(),
        "medium sequence": medium_pattern(),
        "long sequence": long_pattern()
    }

    for key, value in patterns.items():
        print(f"{key}: {value}")


run_task3()
