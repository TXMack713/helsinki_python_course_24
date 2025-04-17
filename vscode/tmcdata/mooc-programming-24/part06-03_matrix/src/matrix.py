# write your solution here
def matrix_sum():
    sum = 0
    sum_list = row_sums()
    for entry in sum_list:
        sum += entry
    return sum

def matrix_max():
    max = 0
    with open("matrix.txt") as file:
        for line in file:
            data = line.split(",")
            for entry in data:
                if int(entry) > max:
                    max = int(entry)
    return max

def row_sums():
    sums = []
    with open("matrix.txt") as file:
        for line in file:
            data = line.split(",")
            sum = 0
            for entry in data:
                sum += int(entry)
            sums.append(sum)
    return sums

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())