# Write your solution here
def first_word(string):
    string_list = []
    string_list = string.split(" ")
    return string_list[0]

def second_word(string):
    string_list = []
    string_list = string.split(" ")
    return string_list[1]
    
def last_word(string):
    string_list = []
    string_list = string.split(" ")
    return string_list[-1]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))