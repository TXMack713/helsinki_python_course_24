# Write your solution here
def longest_series_of_neighbours(num_list: list):
    max_list = []
    current_list = []
    current = 0
    max = 0
    first = 0
    second = 0
    length = len(num_list) - 1
    index = 1
    previous = index - 1 
    while index <= length:
        second = num_list[index]
        first = num_list[previous]
        if (second - first) == 1 or (first - second) == 1:
            if len(current_list) == 0:
                print("Current list", current_list)
                current_list.append(first)
                current_list.append(second)
                if len(current_list) >= len(max_list):
                    max_list = current_list
            else:
                print("Current list", current_list)
                current_list.append(second)
                if len(current_list) >= len(max_list):
                    max_list = current_list
        else:
            if len(current_list) >= len(max_list):
                max_list = current_list
                current_list = []
        index += 1
        previous = index - 1
        # print(max_list)
    return len(max_list)

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
    this_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(this_list))