# Write your solution here
string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

if len(string1) > len(string2):
    print(string1 + " is longer")
elif len(string2) > len(string1):
    print(string2 + " is longer")
elif len(string1) == len(string2):
    print("The strings are equally long")
