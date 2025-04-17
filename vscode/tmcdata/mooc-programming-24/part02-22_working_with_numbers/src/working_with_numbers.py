# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
numbers = []
while True:
    num = int(input("Number: "))
    if num == 0:
        break;
    else:
        numbers.append(num)
    
sum = 0
positives = 0
negatives = 0
count = 0
for x in numbers:
    if x > 0:
        positives += 1
    elif x < 0:
        negatives += 1
    sum += x
    count += 1

mean = sum / count

print("Numbers typed in " + str(count))
print("The sum of the numbers is " + str(sum))
print("The mean of the numbers is " + str(mean))
print("Positive numbers " + str(positives))
print("Negative numbers " + str(negatives))
