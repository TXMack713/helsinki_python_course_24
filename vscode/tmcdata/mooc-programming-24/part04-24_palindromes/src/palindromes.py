# Write your solution here
def palindromes(words):
    list1 = list(words.lower())
    list2 = list(words.lower())
    list2.reverse()
    while True:
        if list1 == list2:
            print(words + " is a palindrome!")
            return True
        else:
            print("that wasn't a palindrome")
            return False
            
# # Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
result = False
while result == False:
    string = input("Please type in a palindrome: ")
    result = palindromes(string)
    if result == True:
        # print(string + " is a palindrome!")
        break
    else:
        # print("that wasn't a palindrome")
        continue
