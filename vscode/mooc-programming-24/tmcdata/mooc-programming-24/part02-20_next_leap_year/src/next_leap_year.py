# Write your solution here
year = input("Year: ")
num_year = int(year)
nextLeapYear = num_year + 1
isLeapYear = False
while not isLeapYear:
    if nextLeapYear % 4 == 0:
        if nextLeapYear % 100 == 0:
            if nextLeapYear % 400 == 0:
                isLeapYear = True
                print(f"The next leap year after {num_year} is {nextLeapYear}")
                break
            else:
                nextLeapYear += 1
        else:
            isLeapYear = True
            print(f"The next leap year after {num_year} is {nextLeapYear}")
            break
    else:
        nextLeapYear += 1



