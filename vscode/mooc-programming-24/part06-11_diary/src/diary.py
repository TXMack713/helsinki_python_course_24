# Write your solution here
def diary():
    file = "diary.txt"
    print("1 - add an entry, 2 - read entries, 0 - quit")
    decision = int(input("Function: "))
    while decision != 0:
        if decision == 1:
            entry = input("Diary entry: ")
            with open(file, "a") as diary_file:
                diary_file.write(entry + "\n")
            print("Diary saved")
            print("")
            print("1 - add an entry, 2 - read entries, 0 - quit")
            decision = int(input("Function: "))
        elif decision == 2:
            with open(file) as diary_file:
                print("Entries:")
                for line in diary_file:
                    print(line)
            print("1 - add an entry, 2 - read entries, 0 - quit")
            decision = int(input("Function: "))
        elif decision != 0 and decision != 1 and decision != 2:
            print("Invalid entry")
            print("1 - add an entry, 2 - read entries, 0 - quit")
            decision = int(input("Function: "))
        # else:
        #     print("Bye now!")
        #     break
    if decision == 0:
        print("Bye now!")

diary()
# if __name__ == "__main__":
#     diary()
