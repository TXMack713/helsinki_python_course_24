# Write your solution here
def find_words(search_term: str):
    all_words = []
    found_words = []
    with open("words.txt") as file:
        for line in file:
            all_words.append(line.strip())
    if "*" in search_term:
        if search_term.startswith("*"):
            for word in all_words:
                if word.endswith(search_term[1:]):
                    found_words.append(word)
        elif search_term.endswith("*"):
            for word in all_words:
                if word.startswith(search_term[:-1]):
                    found_words.append(word)
    elif "." in search_term:
        for word in all_words:
            if len(word) == len(search_term):
                count = 0
                match_count = 0
                char_count = 0
                while count < len(word):
                    if search_term[count] == ".":
                        char_count += 1
                    elif search_term[count] == word[count]:
                        match_count += 1
                    count += 1
                if (match_count + char_count) == len(word):
                    found_words.append(word)
    elif "*" not in search_term and "." not in search_term:
        if search_term in all_words:
            found_words.append(search_term)
    
    return found_words

if __name__ == "__main__":
    print(find_words("c.d."))
    print(find_words(".pple"))
    print(find_words("*pple"))
    print(find_words("apple"))
