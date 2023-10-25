def listen():
    print("Enter a word representing a sound: ")
    word = input()
    print(f"That was a loud {word}!")

listen()

def sighting():
    print("What do you see?? ")
    sight = input()
    if sight == "A large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

sighting()

def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

print("  ")
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
escape_by("digging under")


def cross_bridge(distance):
    for step in range(1, distance + 1):
        print(f"Crossed step {step}")

    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

print("  ")
cross_bridge(3)
cross_bridge(6)

def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

print("  ")
climb_ladder(10, 5)
climb_ladder(5, 10)
