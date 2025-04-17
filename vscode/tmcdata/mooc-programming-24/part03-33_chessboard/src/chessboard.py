# Write your solution here
def chessboard(times):
    char = "1"
    height = 1
    while height <= times:
        length = 1
        string = ""
        while length <= times:
            if char == "0":
                string += char
                char = "1"
            else:
                string += char
                char = "0"
            length += 1
        print(string)
        if string[0] == "1":
            char = "0"
        else:
            char = "1"
        height += 1
    
# Testing the function
if __name__ == "__main__":
    chessboard(3)
