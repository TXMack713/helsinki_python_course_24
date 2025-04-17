# Write your solution here
age = int(input("What is your age? "))

if age < 0:
    print("That must be a mistake")
elif age >= 0 and age < 5:
    print("I suspect you can't write quite yet")
elif age > 120:
    print("Who do you think you are, Methusala?")
else:
    print(f"Ok, you're {age} years old")

