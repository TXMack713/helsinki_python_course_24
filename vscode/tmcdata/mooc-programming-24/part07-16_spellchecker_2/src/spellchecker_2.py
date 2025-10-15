#!/usr/bin/env python3

import re
import difflib

def spell_checker():
    string = input("Please enter a text string of your choosing: ")
    words = string.split(" ")
    dictionary_list = []
    with open("wordlist.txt") as file:
        for line in file:
            dictionary_list.append(line.strip())
    
    # Check for misspelled words
    new_words_list = []
    bad_words_list = []
    for word in words:
        if word.lower() not in dictionary_list:
            word = "*" + word + "*"
            new_words_list.append(word)
            bad_words_list.append(word)
            # print("Bad word", word)
        else:
            new_words_list.append(word)
    
    # Print the entered information with the misspelled words highlighted
    output = ""
    for word in new_words_list:
        output = output + " " + word
    
    print(output.strip())
    print("suggestions:")

    for word in bad_words_list:
        substitute_words = []
        substitute_words = difflib.get_close_matches(word, dictionary_list, n=5, cutoff=0)
        subs_output = ""
        for entry in substitute_words:
            subs_output = subs_output + entry + ", "
        # print(substitute_words)
        print(subs_output[:-2].strip())
 

spell_checker()
