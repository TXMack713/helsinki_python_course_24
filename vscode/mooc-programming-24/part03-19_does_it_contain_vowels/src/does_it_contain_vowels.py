# Write your solution here
line = input("Please type in a string: ")
vowels = ['a', 'e', 'o']
for vowel in vowels:
    if vowel in line:
        print(vowel + " found")
    else:
        print(vowel + " not found")

