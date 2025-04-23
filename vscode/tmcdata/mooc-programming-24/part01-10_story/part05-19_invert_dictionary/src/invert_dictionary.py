# Write your solution here
def invert(dictionary: dict):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    dictionary.clear()
    for key, value in new_dict.items():
        dictionary[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print(s)
    invert(s)
    print("Inverted")
    print(s)