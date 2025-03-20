# Write your solution here
word = input("Please type in a string: ")
index = len(word)
x = index - 1
while 0 <= x:
    print(word[x:index])
    x -= 1
