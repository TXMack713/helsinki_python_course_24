from math import sqrt
# Write your solution here
number = int(input("Please enter a number: "))
condition = True
while condition:    
    if number < 0:
        print("Invalid number")
        number = int(input("Please enter a number: "))
    if number == 0:
        print("Exiting...")
        condition = False
        break
    if number > 0:
        print(sqrt(number))
        number = int(input("Please enter a number: "))


