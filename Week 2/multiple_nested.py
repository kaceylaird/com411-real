location = input("Where should I look? ")

if location == "bedroom":
    sub_location = input("Where in the bedroom? ")
    if sub_location == "under the bed":
        print("Found some shoes but no phone!")
    else:
        print("Found some mess but no phone!")

elif location == "bathroom":
    sub_location = input("Where in the bathroom? ")
    if sub_location == "in the bathtub":
        print("Found a rubber duck but no phone!")
    else:
        print("Found bathroom stuff but no phone!")

elif location == "living room":
    sub_location = input("Where in the living room? ")
    if sub_location == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone!")

else:
    print("I do not know where that is but I will keep looking!!")