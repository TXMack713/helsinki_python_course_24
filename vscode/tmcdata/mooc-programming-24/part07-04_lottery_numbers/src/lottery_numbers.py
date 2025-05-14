# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
    number_list = list(range(lower, upper+1))
    lotto_numbers = random.sample(number_list, amount)
    lotto_numbers.sort()
    return lotto_numbers

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
