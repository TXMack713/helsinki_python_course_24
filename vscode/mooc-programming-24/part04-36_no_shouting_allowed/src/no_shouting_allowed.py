# Write your solution here
def no_shouting(string_list: list):
    new_list = []
    for x in string_list:
        if x.isupper() == True:
            continue
        else:
            new_list.append(x)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
