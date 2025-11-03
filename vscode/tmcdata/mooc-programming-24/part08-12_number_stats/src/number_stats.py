#!/usr/bin/env python 3

class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if len(self.numbers) == 0:
            return 0
        else:
            sum = 0
            for num in self.numbers:
                sum += num
            return sum
    
    def average(self):
        if len(self.numbers) == 0:
            return 0
        else:
            sum = self.get_sum()
            average = sum / len(self.numbers)
            return average


status = True
evens = NumberStats()
odds = NumberStats()
entries = NumberStats()
while status:
    try:
        entry = int(input("Please enter a whole number: "))
        if entry != -1:
            if entry % 2 == 0:
                evens.add_number(entry)
                entries.add_number(entry)
            else:
                odds.add_number(entry)
                entries.add_number(entry)
        else:
            print("Sum of numbers:", entries.get_sum())
            print("Mean of numbers:", entries.average())
            print("Sum of even numbers:", evens.get_sum())
            print("Sum of odd numbers:", odds.get_sum())
            status = False
    except:
        print("That was an invalid entry: ")


