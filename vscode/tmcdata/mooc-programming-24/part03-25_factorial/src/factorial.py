# Write your solution here
while True:
    sum = 1
    number = int(input("Please type in a number: "))
    orig = number
    if number <= 0:
        print("Thanks and bye!")
        break
    else:
        while number > 0:
            sum *= number
            number -= 1 
        print("The factorial of the number " + str(orig) + " is " + str(sum))

