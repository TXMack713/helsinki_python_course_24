# Write your solution here
integer = int(input("Please type in a positive integer: "))
negative = (-1) * integer
for x in range (negative, integer + 1):
    if x == 0:
        continue
    else:
        print(x)

