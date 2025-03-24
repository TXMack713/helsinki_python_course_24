# Write your solution here
def distinct_numbers(nums):
    unique = []
    for x in nums:
        if unique.count(x) == 0:
            unique.append(x)
    unique.sort()
    return unique

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
