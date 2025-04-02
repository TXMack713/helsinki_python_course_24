# Write your solution here
def anagrams(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
    # list1 = ["m", "a", "t", "e"]
    # list2 = ["m", "a", "t", "e"]
    # list1.sort()
    # list2.sort()
    # print(list1 == list2)
    # print(list1)
    # print(list2)