# Write your solution here
line = input("Please type in a string: ")
if line[1] == line[-2]:
    print("The second and the second to last characters are " + line[1])
else:
    print("The second and the second to last characters are different")
