# Write your solution here
from datetime import datetime

def get_date():
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    # birth = datetime(year, month, day)
    return (day, month, year)

def calculate_days():
    birthdate = get_date()
    birth = datetime(birthdate[2], birthdate[1], birthdate[0])
    print(birth)
    # Calculate the millenium
    millenium = datetime(1999,12,31)
    print(millenium)

    difference = millenium - birth
    print(difference)

    result = difference.days

    if result > 0:
        print("You were " + str(result) + " days old on the eve of the new millennium.")
    else:
        print("You weren't born yet on the eve of the new millennium.")
    
    # return difference

if __name__ == "__main__":
    calculate_days()

