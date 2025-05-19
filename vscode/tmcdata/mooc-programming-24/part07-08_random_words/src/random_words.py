# Write your solution here
import random
def words(n: int, beginning: str):
    all_words = []
    string_words = []
    with open("words.txt") as file:
        for line in file:
            entry = line.strip("\n")
            all_words.append(entry)
        all_words.sort()
        all_words.reverse()
    
    for word in all_words:
        if word.startswith(beginning):
            string_words.append(word)
    
    # counter = 2 * n
    sample_words = random.sample(string_words, n)
    if len(sample_words) < n:
        raise ValueError
    
    found_words = random.sample(sample_words, n)
       
    return found_words

if __name__ == "__main__":
    word_list = words(3, "hi")
    for word in word_list:
        print(word)
