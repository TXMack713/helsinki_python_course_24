# Write your solution here
def factorials(n: int):
    my_dict = {}
    count = 1
    sum = 1
    while count <= n:
        sum *= count
        my_dict[count] = sum
        count += 1
    # print(my_dict)
    return my_dict

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])