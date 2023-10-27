def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run():
    print(f"Minimum likelihood of falling: {likelihood()}%")


if __name__ == "__main__":
    run()


def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task1():
    probabilities = likelihood_min_max()
    print(f"Minimum likelihood of falling: {probabilities[0]}%")
    print(f"Maximum likelihood of falling: {probabilities[1]}%")


if __name__ == "__main__":
    run_task1()


def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run():
    all_steps = steps()
    good_steps = []
    bad_steps = []

    for step in all_steps:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")


if __name__ == "__main__":
    run()
