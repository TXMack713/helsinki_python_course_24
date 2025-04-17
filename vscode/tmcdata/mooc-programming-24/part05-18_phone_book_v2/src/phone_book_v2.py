# Write your solution here
phone_book = {}

def command():
    while True:
        num = int(input("command (1 search, 2 add, 3 quit): "))
        # print("you entered:", num)
        if num == 1:
            name = input("name: ")
            search(name)
            continue
        elif num == 2:
            name = input("name: ")
            number = input("number: ")
            add(name, number)
            continue
        elif num == 3:
            print("quitting...")
            break

def search(name):
    # print("name: ", name)
    if name in phone_book:
        if len(phone_book[name]) > 1:
            for x in phone_book[name]:
                print(x)
        else:
            print(phone_book[name][0])
    else:
        print("no number")

def add(name, number):
    if name not in phone_book:
        phone_book[name] = []
        phone_book[name].append(number)
    else:
        phone_book[name].append(number)
    print("ok!")

command()
# if __name__ == "__main__":
#     command()
    