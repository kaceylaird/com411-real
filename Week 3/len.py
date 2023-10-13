phrase = input("Please enter a phrase: ")
wordCount = 0
while wordCount < len(phrase):
    wordCount += 1
    print(f"{phrase}")

count = 1
total = 0

print("Calculating the sum of the first 100 numbers...")

while count <= 100:
    total += count
    count += 1

print("...Done! The answer is", total)


total = 0
num_numbers = int(input("How many numbers should I sum up? "))

count = 0
while count < num_numbers:
    try:
        number = float(input("Enter a number: "))
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("The answer is", total)










