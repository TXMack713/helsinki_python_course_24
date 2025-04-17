
# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
indexes = []
b = len(word)
c = 0
for x in word:
    if x == character:
        indexes.append(c)
    c += 1
# index = word.find(character)
stoppage = 0
for y in indexes:
    stoppage = y + 3
    substring = word[y:stoppage]
    if len(substring) == 3:
        print(substring)
