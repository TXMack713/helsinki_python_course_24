# Write your solution here
def all_the_longest(words):
    temp = []
    length = 0
    for x in words:
        if len(x) >= length:
            temp.append(x)
            length = len(x)
    final = []
    for x in temp:
        if len(x) >= length:
            final.append(x)
    return final

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
