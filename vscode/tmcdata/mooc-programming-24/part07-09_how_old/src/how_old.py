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
    birth = datetime(birthdate[0], birthdate[1], birthdate[2])
    # Calculate the millenium
    millenium = datetime(1999,12,31)

    difference = millenium - birth

    result = difference.days

    if result > 0:
        print("You were " + str(result) + " days old on the even of the new millennium.")
    else:
        print("You weren't born yet on the even of the new millennium.")
    
    # return difference

if __name__ == "__main__":
    calculate_days()

    
