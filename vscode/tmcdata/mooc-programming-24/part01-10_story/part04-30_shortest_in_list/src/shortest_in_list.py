def shortest(words):
    shortest = 0
    shortest_word = ""
    for x in words:
        if shortest == 0:
            shortest = len(x)
            shortest_word = x
        elif len(x) <= shortest:
            shortest_word = x
            shortest = len(x)
    return shortest_word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)