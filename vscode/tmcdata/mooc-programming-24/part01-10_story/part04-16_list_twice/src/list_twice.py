# Write your solution here
my_list = []
sorted = []
item = int(input("New item: "))
while True:
    if item == 0:
        print("Bye!")
        break
    else:
        my_list.append(item)
        sorted.append(item)
        print("The list now:", sorted) 
        my_list.sort()
        print("The list in order:", my_list)
        # my_list = sorted
        item = int(input("New item: "))
