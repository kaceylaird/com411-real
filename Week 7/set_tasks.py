def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


run_task1()


def observed():
    observations = []

    for count in range(7):
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
