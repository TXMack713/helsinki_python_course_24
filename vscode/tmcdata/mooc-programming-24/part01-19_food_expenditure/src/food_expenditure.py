# Write your solution here
num_of_dines = int(input("How many times a week do you eat the student cafeteria?"))
price = float(input("What is the price of a typical lunch?"))
grocery_total = float(input("How much do you spend on groceries in a week?"))

print("Average food expenditrure:")
print(f"Daily: {(price * num_of_dines + grocery_total) / 7} euros")
print(f"Weekly: {price * num_of_dines + grocery_total} euros")