# Write your solution here
gift = int(input("Value of gift: "))
tax = 0

if gift < 5000:
    print("No tax!")
elif 5000 <= gift <= 25000:
    tax = 100 + (gift-5000)*.08
    print(f"Amount of tax: {tax}")
elif 25000 < gift <= 55000:
    tax = 1700 + (gift-25000)*.1
    print(f"Amount of tax: {tax}")
elif 55000 < gift <= 200000:
    tax = 4700 + (gift-55000)*.12
    print(f"Amount of tax: {tax}")
elif 200000 < gift <= 1000000:
    tax = 22100 + (gift-200000)*.15
    print(f"Amount of tax: {tax}")
elif gift > 1000000:
    tax = 142100 + (gift-1000000)*.17
    print(f"Amount of tax: {tax}")

