# Copy here code of line function from previous exercise and use it in your solution
def line(num, text):
    if text == "":
        print("*"*num)    
    elif len(text) >= 1:
       print(num*text[0])

def triangle(size, char):
    # You should call function line here with proper parameters
    count = 1
    while count <= size:
        line(count, char)
        count += 1

def shape(width, tri_char, height, rect_char):
    triangle(width, tri_char)
    count = 1
    while count <= height:
        line(width, rect_char)
        count += 1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")