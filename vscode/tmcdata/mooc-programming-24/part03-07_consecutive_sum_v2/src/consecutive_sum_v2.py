# Write your solution here
limit = int(input("Limit: "))
counter = 1
sum = 0
phrase = "The consecutive sum: "
while sum < limit:
    sum += counter
    phrase += str(counter)
    counter += 1
    if sum < limit:
        phrase += " + "
phrase += " = " + str(sum)
print(phrase)
