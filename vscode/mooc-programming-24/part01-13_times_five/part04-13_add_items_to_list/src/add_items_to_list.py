# Write your solution here
number_of_items = int(input("How many items: "))
count = 1
list = []
while count <= number_of_items:
    item = int(input("Item " + str(count) + ": "))
    list.append(item)
    count += 1
print(list)