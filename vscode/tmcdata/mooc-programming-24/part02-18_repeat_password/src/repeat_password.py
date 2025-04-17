# Write your solution here
password = input("Please enter a password: ")
second = input("Please enter the password again: ")
condition = True
while condition:
    if (password == second):
        print("User account created!")
        condition = False
    else:
        print("They do not match!")
        second = input("Please enter the password again: ")

