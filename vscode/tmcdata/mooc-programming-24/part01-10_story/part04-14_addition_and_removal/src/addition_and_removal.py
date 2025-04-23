# Write your solution here
list = []
while True:
    print("The list is now", list)
    choice = input("a(d)d, (r)emove, e(x)it: ")
    if choice.lower() == "d":
        if len(list) == 0:
            list.append(1)
        else:
            list.append(list[-1]+1)
    elif choice.lower() == "r":
        if len(list) == 0:
            continue
        else:
            list.pop(-1)
    elif choice.lower() == "x":
        print("Bye!")
        break
