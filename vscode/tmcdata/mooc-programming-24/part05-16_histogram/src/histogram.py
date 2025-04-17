# Write your solution here
def histogram(words):
    letters = {}
    for letter in words:
        if letter not in letters:
            letters[letter] = ""
            letters[letter] += "*"
        else:
            letters[letter] += "*"
    for key, value in letters.items():
        print(key, value)
    
if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")

