# Write your solution here
def squared(string, times):
    span = len(string) - 1
    
    height = 1
    index = 0
    while height <= times:
        length = 1
        text = ""
        while length <= times:
            if index <= span:
                text += string[index]
                index += 1
            else:
                index = 0
                text += string[index]
                index += 1
            length += 1
        print(text)
        height += 1


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)