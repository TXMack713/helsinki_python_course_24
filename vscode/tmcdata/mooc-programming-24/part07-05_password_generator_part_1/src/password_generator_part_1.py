# Write your solution here
import random
import string
def generate_password(length: int):
    alpha_list = string.ascii_lowercase
    letters = random.sample(alpha_list, length)
    password = ""
    for letter in letters:
        password += letter
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
