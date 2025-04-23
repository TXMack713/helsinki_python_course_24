# Write your solution here
word = input("Please type in a string: ")
substring = input("Please type in a substring: ")
# indexes = []
b = len(substring)
first_index = word.find(substring)
new_sub = word[(first_index+b):]
# print(word)
# print(new_sub)
second_index = new_sub.find(substring)
# print("First index: " + str(first_index))
# print("Second index: " + str(second_index))

if second_index != -1:
    print("The second occurrence of the substring is at index " + str(first_index+second_index+len(substring)) + ".")
else:
    print("The substring does not occur twice in the string.")

