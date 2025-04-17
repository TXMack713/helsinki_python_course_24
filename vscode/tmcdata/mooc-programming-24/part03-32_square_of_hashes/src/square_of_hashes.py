# Write your solution here
def hash_square(num):
    length = 1
    height = 1
    while height <= num:
        while length <= num:
            print("#"*num)
            length += 1
        height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)