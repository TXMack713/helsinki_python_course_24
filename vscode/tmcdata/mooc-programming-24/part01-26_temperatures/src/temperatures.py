# Write your solution here
fahr = int(input("Please enter a temperature: "))
cel = (fahr-32) * (5/9)
print(f"{fahr} degrees Fahrenheit equals {cel} degrees Celsius")
if cel < 0:
    print("Brr! It's cold in here!")

