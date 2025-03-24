# Write your solution here
def no_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = string
    for x in vowels:
        new_string = new_string.replace(x, "")
    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
