# Write your solution here
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")

if day.lower() == "sunday":
    print(f"Daily wages: {wage * hours * 2} euros")

if day.lower() != "sunday":
    print(f"Daily wages: {wage * hours} euros")

