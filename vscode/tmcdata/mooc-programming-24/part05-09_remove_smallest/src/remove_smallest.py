# Write your solution here
def remove_smallest(numbers: list):
    compare = []
    for x in numbers:
        compare.append(x)
    compare.sort()
    numbers.remove(compare[0])

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)