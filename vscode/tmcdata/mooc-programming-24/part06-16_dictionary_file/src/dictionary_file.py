# Write your solution here
word_dictionary = {}
with open("dictionary.txt", "a") as file:
    for line in file:
        array = []
        array = line.split(" ")
        word_dictionar1y[array[0]] = array[1]
        
def dictionary():
    answer = True
    while answer:
        response = prompt()
        if response == 3:
            answer = False
            print("Bye!")
            break
        elif response == 2:
            term = input("Search term: ")
            for key, value in word_dictionary.items():
                if key.find(term) != -1 or value.find(term) != -1:
                    print(key + " - " + value)
        elif response == 1:
            finn = input("The word in Finnish: ")
            eng = input("The word in English: ")
            word_dictionary[finn] = eng
            print("Dictionary entry added")
            # response = prompt()
    with open("dictionary.txt", "a") as file:
        for key, value in word_dictionary.items():
            file.write(key + " - " + value)

def prompt():
    print("1 - Add word, 2 - Search, 3 - Quit")
    entry = int(input("Function: "))
    return entry

dictionary()