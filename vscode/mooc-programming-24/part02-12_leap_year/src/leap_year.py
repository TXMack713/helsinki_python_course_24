# Write your solution here
year = int(input("Please type in a year: "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

    