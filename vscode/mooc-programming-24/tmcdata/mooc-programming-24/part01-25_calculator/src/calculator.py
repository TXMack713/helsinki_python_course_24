# Write your solution here
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
operation = input("Please enter the operation: ")
operation = operation.lower()
if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")

if operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")

if operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")

