# Write your solution here
word = ""
words = []
while True:
    word = input("Word: ")
    if word in words:
        print("You typed in " + str(len(words)) + " different words")
        break
    else:
        words.append(word)


