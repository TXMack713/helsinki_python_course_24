# Write your solution here
#!/usr/bin/env python3
from datetime import datetime, date

filename = input("Please enter the file name: ")
entry = input("Please enter the starting date in this format, dd.mm.YYYY: ")
entry_array = entry.split(".")
entry_array[0] = int(entry_array[0])
entry_array[1] = int(entry_array[1])
entry_array[2] = int(entry_array[2])

print(f"Date split: {entry_array}")
start_date = ""

# validate date
while True:
    try:
        start_date = date(entry_array[2],entry_array[1],entry_array[0]).strftime("%d.%m.%Y")
        print(start_date)
        # print(start_date.strftime("%d.%m.%Y"))
        break
    except:
        print("Invalid date")
        start_date = date(entry_array[2],entry_array[1],entry_array[0]).strftime("%d.%m.%Y")
        print("Date entered: " + start_date)
        entry = input("Please enter the starting date in this format, dd.mm.YYYY: ")
        entry_array = entry.split(".")
        date_text = entry_array[2] + "-" + entry_array[1] + "-" + entry_array[0]

number_of_days = int(input("How many days: "))

time_input = []
all_time_entries = []
days = []

print("Please type in screen time in minutes on each day (TV computer mobile) separated by spaces:")

# Collect the amount of time spent on screens for each day including the start date
counter = 0
while counter < number_of_days:
    # Collect information for the current date and validate the date
    this_date = ""
    try:
        this_date = date(entry_array[2],entry_array[1],entry_array[0]).strftime("%d.%m.%Y")
        
    except:
        try:
            entry_array[1] += 1
            entry_array[0] = 1
            this_date = date(entry_array[2],entry_array[1],entry_array[0]).strftime("%d.%m.%Y")
        except:
            entry_array[2] += 1
            entry_array[1] = 1
            entry_array[0] = 1
            # date_text = entry_array[2] + "-" + entry_array[1] + "-" + entry_array[0]
            this_date = date(entry_array[2],entry_array[1],entry_array[0]).strftime("%d.%m.%Y")
    entry = input(f"Screen time {this_date}: ")
    time_input = entry.split(" ")
    all_time_entries.append(time_input)
    days.append(this_date)
    entry_array[0] += 1
    counter += 1

total_minutes = 0
average_minutes = 0
for time_entered in all_time_entries:
    for minutes in time_entered:
        total_minutes += int(minutes)
    
average_minutes = total_minutes / number_of_days

# Write the information to the file
with open(filename, "w") as file:
    file.write(f"Time period: {days[0]}-{days[-1]}"+"\n")
    file.write(f"Total minutes: {total_minutes}"+"\n")
    file.write(f"Average minutes: {average_minutes}"+"\n")
    # Check file input manually
    print(f"Time period: {days[0]}-{days[-1]}")
    print(f"Total minutes: {total_minutes}")
    print(f"Average minutes: {average_minutes}")
    counter = 0
    while counter < number_of_days:
        file.write(f"{days[counter]}: {all_time_entries[counter][0]}/{all_time_entries[counter][1]}/{all_time_entries[counter][2]}"+"\n")
        counter += 1

