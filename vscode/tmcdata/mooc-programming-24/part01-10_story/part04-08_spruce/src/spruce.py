# Write your solution here
def spruce(num):
    chars = 1
    count = 1
    extra = int(num / 2)*2
    width = num + extra
    whitespace = width - chars
    half = int(whitespace / 2)
    print("a spruce!")
    while count <= num:
        print((half*" ") + (chars*"*") + (half*" "))
        chars += 2
        count += 1
        whitespace = width - chars
        half = int(whitespace / 2)
    chars = 1
    whitespace = width - chars
    half = int(whitespace / 2)
    print((half*" ") + (chars*"*") + (half*" "))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)