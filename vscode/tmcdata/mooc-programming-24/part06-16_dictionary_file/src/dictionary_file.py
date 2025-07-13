# Write your solution here
word_dictionary = {}
added_words = {}
def read_dictionary():    
    with open("dictionary.txt") as file:
        for line in file:
            array = []
            line = line.strip()
            array = line.split("-")
            if len(array) > 1:
                word_dictionary[array[0].strip()] = array[1].strip()
            else:
                continue
    # return word_dictionary
        
def dictionary():
    read_dictionary()
    answer = True
    while answer:
        response = prompt()
        if response == 3:
            answer = False
            print("Bye!")
            with open("dictionary.txt", "a") as file:
                for key, value in added_words.items():
                    file.write(key + " - " + value + "\n")
            break
        elif response == 2:
            term = input("Search term: ")
            search_dictionary = {}
            with open("dictionary.txt") as file:
                for line in file:
                    array = []
                    line = line.strip()
                    array = line.split("-")
                    if len(array) > 1:
                        search_dictionary[array[0].strip()] = array[1].strip()
                    else:
                        continue
            for key, value in search_dictionary.items():
                if key.find(term) != -1 or value.find(term) != -1:
                    print(key + " - " + value)
        elif response == 1:
            finn = input("The word in Finnish: ")
            eng = input("The word in English: ")
            for key, value in word_dictionary.items():
                added_words[finn] = eng
            print("Dictionary entry added")
            # response = prompt()
            with open("dictionary.txt", "a") as file:
                # for key, value in word_dictionary.items():
                file.write(finn + " - " + eng + "\n")

def prompt():
    print("1 - Add word, 2 - Search, 3 - Quit")
    entry = int(input("Function: "))
    return entry

dictionary()
