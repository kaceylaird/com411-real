num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third number: "))


even_count, odd_count = 0,0

if num1 % 2 == 0:
    even_count += 1

else:
    odd_count += 1

if num2 % 2 == 0:
    even_count += 1

else:
    odd_count += 1

if num3 % 2 == 0:
    even_count += 1

else:
    odd_count += 1

print(f"There were {odd_count} odd numbers and {even_count} even numbers.")
