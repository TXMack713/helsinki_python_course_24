# Write your solution here
def length_of_longest(words):
    longest = 0
    max_word = ""
    for x in words:
        if len(x) > longest:
            max_word = x
            longest = len(x)
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)