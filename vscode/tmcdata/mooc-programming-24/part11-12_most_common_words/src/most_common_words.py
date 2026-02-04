#!/usr/bin/env python 3

def most_common_words(filename: str, lower_limit: int):
    all_words = []
    with open(filename) as file:
        for line in file:
            words = line.split(" ")
            for word in words:
                all_words.append(word.strip("!,.?\n"))
    return {word : all_words.count(word) for word in all_words if all_words.count(word) >= lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
