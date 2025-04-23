# Write your solution here
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

if number1 > number2:
    print(f"The greater number was: {number1}")
elif number2 > number1:
    print(f"The greater number was: {number2}")
elif number1 == number2:
    print("The numbers are equal!")

