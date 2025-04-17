# Write your solution here
editor = input("What editor are you using? ")
editor = editor.lower()

while True:
    if editor != "visual studio code":
        if editor == "word":
            print("awful")
        else:
            print("not good")
        editor = input("What editor are you using? ")
        editor = editor.lower()
    else:
        print("an excellent choice!")
        break

