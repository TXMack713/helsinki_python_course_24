#!/usr/bin/env python 3

import re

def is_dotw(my_string: str):
    criteria = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(criteria, my_string):
        return True
    else:
        return False
    
def all_vowels(my_string: str):
    criteria = "^[aeiou]*$"
    if re.search(criteria, my_string):
        return True
    else:
        return False
    
def time_of_day(my_string: str):
    criteria1 = "[0-1][0-9]:[0-5][0-9]:[0-5][0-9]"
    criteria2 = "[2][0-3]:[0-5][0-9]:[0-5][0-9]"
    if re.search(criteria1, my_string):
        return True
    elif re.search(criteria2, my_string):
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    print("")

    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    print("")

    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
