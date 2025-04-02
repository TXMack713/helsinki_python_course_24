# write your solution here
def largest():
    numbers = []
    with open("numbers.txt") as file:
        entry = int(file.readline())
        numbers.append(entry)

    most = 0
    count = 0
    counted_numbers = {}
    for item in numbers:
        if item not in counted_numbers:
            counted_numbers[item] = 1
        else:
            counted_numbers[item] += 1
    for key in counted_numbers:
        if counted_numbers[key] > count:
            count = counted_numbers[key]
            most = key

    return most

if __name__ == "__main__":
    largest()