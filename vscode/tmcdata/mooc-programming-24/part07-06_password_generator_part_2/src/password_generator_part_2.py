# Write your solution here
import random
import string
def generate_strong_password(length: int, nums: bool, chars: bool):
    alpha_list = string.ascii_lowercase
    alphanum_list = string.ascii_lowercase + string.digits
    puncs = "!?=+-()#"
    all_list = string.ascii_lowercase + string.digits + puncs
    alpha_char_list = string.ascii_lowercase + puncs
    letters = []
    if nums == False and chars == False:
        letters = random.sample(alpha_list, length)
    elif nums == True and chars == False:
        letters = random.sample(alphanum_list, length)
        count = 0
        while True:
            for letter in letters:
                if letter.isnumeric():
                    count += 1
            if count == 0:
                letters = random.sample(alphanum_list, length)
            else:
                break
    elif nums == True and chars == True:
        letters = random.sample(all_list, length)
        letter_count = 0
        num_count = 0
        char_count = 0
        while True:
            for letter in letters:
                if letter.isalpha():
                    letter_count += 1
                if letter.isnumeric():
                    num_count += 1
                for item in puncs:
                    if letter == item:
                        char_count += 1
            if num_count == 0 or char_count == 0 or letter_count == 0:
                letters = random.sample(all_list, length)
            else:
                break
    elif nums == False and chars == True:
        letters = random.sample(alpha_char_list, length)
        letter_count = 0
        # num_count = 0
        char_count = 0
        while True:
            for letter in letters:
                if letter.isalpha():
                    letter_count += 1
                for item in puncs:
                    if letter == item:
                        char_count += 1
            if char_count == 0 or letter_count == 0:
                letters = random.sample(alpha_char_list, length)
            else:
                break

    password = ""
    for letter in letters:
        password += letter
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
