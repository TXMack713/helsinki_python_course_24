#!/usr/bin/env python 3

def prime_numbers():
    number = 1
    divider = 1
    counter = 0
    while True:
        if number % divider == 0 and divider != 1 and divider != number:
            counter = 0
            divider = 1
            number += 1
        elif number % divider == 0:
            counter += 1
            divider += 1
        elif divider >= number and counter == 2:
                prime = number
                divider = 1
                number += 1
                counter = 0
                yield prime
        elif divider >= number:
                divider = 1
                number += 1
                counter = 0
        else:
            divider += 1

 
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))

