def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


run_task1()


def observed():
    observations = []

    for count in range(7):
        count += 1
        print("Please enter an observation:")
        observations.append(input())
        return observations


def run_task2():
    print("Counting observations...")
    observations = observed()

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times.")


run_task2()


def observed_items():
    observations = []

    for count in range(5):
        print("Please enter an observation: ")
        observations.append(input())

        return observations


def remove_observations(observations):
    is_running = True

    while is_running:
        print("Do you wish to remove an observation? (Yes/No)")
        response = input()

        if response == "Yes":
            print("Please enter the observation that you wish to remove: ")
            observation = input()
            observations.remove(observation)
        else:
            is_running = False


def run_task3():
    observations = observed()
    remove_observations(observations)

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times.")


run_task3()
