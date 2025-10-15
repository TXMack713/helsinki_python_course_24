#!/usr/bin/env python3

def spell_checker():
    string = input("Please enter a text string of your choosing: ")
    words = string.split(" ")
    dictionary_list = []
    with open("wordlist.txt") as file:
        for line in file:
            dictionary_list.append(line.strip())
    
    # Check for misspelled words
    new_words_list = []
    for word in words:
        if word.lower() not in dictionary_list:
            word = "*" + word + "*"
            new_words_list.append(word)
            # print("Bad word", word)
        else:
            new_words_list.append(word)
    
    # Print the entered information with the misspelled words highlighted
    output = ""
    for word in new_words_list:
        output = output + " " + word
    
    
    print(output.strip())

spell_checker()
