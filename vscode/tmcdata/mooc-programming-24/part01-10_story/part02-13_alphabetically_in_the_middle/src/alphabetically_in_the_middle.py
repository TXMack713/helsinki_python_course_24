# Write your solution here.
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

letters = [letter1, letter2, letter3]
letters.sort()

print(f"The letter in the middle is {letters[1]}")
