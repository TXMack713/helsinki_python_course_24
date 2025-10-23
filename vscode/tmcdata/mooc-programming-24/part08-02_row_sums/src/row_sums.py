#!/usr/bin/env python3

def row_sums(my_matrix: list):
    new_list = []
    for row in my_matrix:
        sum = 0
        for entry in row:
            sum += entry
        row.append(sum)

if __name__ == "__main__":
    my_matrix = [[1,2], [3,4]]
    row_sums(my_matrix)
    print(my_matrix)

# Write your solution here
