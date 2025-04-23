# Write your solution here
def same_chars(string, num1, num2):
    if num1 >= len(string) or num2 >= len(string):
        # print("False block,", False)
        return False
    elif string[num1] == string[num2]:
        # print("True block,", True)
        return True
    else:
        # print("False block again,", False)
        return False

    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))
    print(same_chars("hello", 2, 3))