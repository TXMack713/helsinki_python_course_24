# Write your solution here
number = int(input("Please type in a number: "))
count = 1
arr = []
while count <= number:
    arr.append(count)
    count += 1
spanner = round(number / 2) + 1
# print(spanner)
# print("Spanner")
index = 0
backwards_index = -1
counts = 1
while len(arr) > 0:
    print(arr[index])
    arr.pop(index)
    if len(arr) > 1:
        print(arr[backwards_index])
        arr.pop(backwards_index)
    counts += 1
    # index += 1
    # backwards_index -= 1

