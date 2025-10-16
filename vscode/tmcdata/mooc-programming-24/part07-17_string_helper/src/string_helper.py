#!/usr/bin/env python3

def change_case(orig_string: str):
    new_string = ""
    for item in orig_string:
        if item.islower():
            item = item.upper()
            new_string += item
        elif item.isupper():
            item = item.lower()
            new_string += item
        else:
            new_string += item
    return new_string

def split_in_half(orig_string: str):
    half = len(orig_string) // 2
    first = orig_string[:half]
    second = orig_string[half:]
    final = (first, second)
    return final

def remove_special_characters(orig_string: str):
    new_string = ""
    for item in orig_string:
        if item.isalnum() or item.isspace():
            new_string += item
        else:
            continue
    return new_string

if __name__ == "__main__":
    print(change_case("This is a test of the change case method!"))
    print(split_in_half("First and second"))
    print(remove_special_characters("This! is a test, of the change* case! method?"))
