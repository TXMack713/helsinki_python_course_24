# Write your solution here
def sum_of_positives(int_list):
    sum = 0
    for x in int_list:
        if x > 0:
            sum += x
    return sum

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)