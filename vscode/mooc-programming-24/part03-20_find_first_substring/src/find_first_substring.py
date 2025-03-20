# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)
stoppage = index + 3
substring = word[index:stoppage]
if len(substring) == 3:
    print(substring)

