# Write your solution here
import string
def separate_characters(my_string: str):
    letters = ""
    punctuations = ""
    all_others = ""
    for item in my_string:
        if item in string.ascii_letters:
            letters += item
        elif item in string.punctuation:
            punctuations += item
        else:
            all_others += item
        
    return(letters, punctuations, all_others)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
