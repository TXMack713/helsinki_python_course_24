# Copy here code of line function from previous exercise
def line(num, text):
    if text == "":
        print("*"*num)    
    elif len(text) >= 1:
        print(num*text[0])

def box_of_hashes(height):
    # You should call function line here with proper parameters
    count = 0
    while count < height:
        line(10, "#")
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
