# Write your solution here
def times_ten(start_index: int, end_index: int):
    tens_dict = {}
    count = start_index
    while count <= end_index:
        tens_dict[count] = count * 10
        count += 1
    return tens_dict

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)