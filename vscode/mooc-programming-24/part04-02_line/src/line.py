# Write your solution here
def line(num, text):
    # height = 1
    # length = 1
    if text == "":
        print("*"*num)    
    elif len(text) >= 1:
        print(num*text[0])
    # height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")