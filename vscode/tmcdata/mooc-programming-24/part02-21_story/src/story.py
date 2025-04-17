# Write your solution here
word = input("Please type in a word: ")
last_word = ""
phrase = []
while True:
    if word == "end":
        break;
    elif word == last_word:
        break;
    else:
        last_word = word
        phrase.append(word)
            # print(word)
            # print(last_word)
            # print(phrase)
        word = input("Please type in a word: ")

text = ""
for x in phrase:
    text = text + x + " "

print(text)

