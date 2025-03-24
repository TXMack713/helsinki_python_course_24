# Write your solution here
def formatted(the_list):
    new_list = []
    for x in the_list:
        change = f"{x:.2f}"
        new_list.append(change)
    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
