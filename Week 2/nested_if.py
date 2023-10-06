cover = input("Is the book hard or soft shell? ")

if cover == "soft":
    perfect_bound = input("Is the book perfect bound? ")

    if perfect_bound == "yes":
        print("Soft cover, perfect-bound books are very popular!")

    else:
        print("Soft covers with coils or stitches are great for short books!")

else:
    print("Hard cover books can be more expensive!")