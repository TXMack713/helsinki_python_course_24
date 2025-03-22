# Copy here code of line function from previous exercise
def line(num, text):
    if text == "":
        print("*"*num)    
    elif len(text) >= 1:
        print(num*text[0])

def square(size, character):
    # You should call function line here with proper parameters
    count = 0
    while count < size:
        line(size, character)
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")