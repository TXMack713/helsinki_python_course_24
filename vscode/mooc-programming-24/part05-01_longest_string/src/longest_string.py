# Write your solution here
def longest(strings):
    length = 0
    string = ""
    for x in strings:
        if len(x) >= length:
            length = len(x)
            string = x
    return string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
