#!/usr/bin/env python 3

def recursive_sum(number: int):
    if number <= 1:
        return number
    else:
        sum = number + recursive_sum(number - 1)
        return sum

if __name__ == "__main__":
    result = recursive_sum(3)
    print(result)

    print(recursive_sum(5))
    print(recursive_sum(10))
