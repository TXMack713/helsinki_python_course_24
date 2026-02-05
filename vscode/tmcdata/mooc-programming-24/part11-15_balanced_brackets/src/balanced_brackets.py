#!/usr/bin/env python 3

def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    if len(my_string) == 1 and my_string[0] in "()[]":
        return False
    if my_string[0] == "(":
        if (my_string[-1].isascii() and my_string[-1] not in "()[]"):
            return balanced_brackets(my_string[:-1])
        if not (my_string[0] == '(' and my_string[-1] == ')'):
            return False
    if my_string[0] == "[":
        if (my_string[-1].isascii() and my_string[-1] not in "()[]"):
            return balanced_brackets(my_string[:-1])
        if not (my_string[0] == '[' and my_string[-1] == "]"):
            return False
        
    # remove the first character
    if (my_string[0].isascii() and my_string[0] not in "()[]") and (my_string[-1] == ")" or my_string[-1] == "]"):
        return balanced_brackets(my_string[1:])
    
    # remove the last character
    if (my_string[-1].isascii() and my_string[-1] not in "()[]") and (my_string[0] == "(" or my_string[0] == "["):
        return balanced_brackets(my_string[:-1])
    
    # remove first and last character
    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("(((())))")
    print(ok)

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)

    print("---------------------")

    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

    ok = balanced_brackets("(x)y)")
    print(ok)

