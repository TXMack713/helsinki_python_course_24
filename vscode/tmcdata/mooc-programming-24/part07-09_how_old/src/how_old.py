# Write your solution here
from datetime import datetime

def get_date():
    day = int(input("Day:"))
    month = int(input("Month:"))
    year = int(input("Year:"))
    # birth = datetime(year, month, day)
    return (day, month, year)

def calculate_days():
    birthdate = get_date()
    birth = datetime(birthdate[2], birthdate[1], birthdate[0])

    # Calculate the millenium
    millenium = datetime(1999,12,31)

    difference = millenium - birth

    result = difference.days
    answer = ""

    if result > 0:
        answer = "You were " + str(result) + " days old on the eve of the new millennium."
    else:
        answer = "You weren't born yet on the eve of the new millennium."
    
    return answer

print(calculate_days())

