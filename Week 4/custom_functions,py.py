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