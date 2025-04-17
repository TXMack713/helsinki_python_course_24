# Write your solution here
number = int(input("Please type in a number: "))
orig_arr = []
new_arr = []
count = 1
while count <= number:
    orig_arr.append(count)
    new_arr.append(count)
    count += 1
# print(orig_arr)
x = 0
while x < number:
    if x+1 < number:
        new_arr[x] = orig_arr[x+1]
        # print(new_arr[x])
        new_arr[x+1] = orig_arr[x]
        # print(new_arr[x+1])
    else:
        break
    x += 2

for num in new_arr:
    print(num)
