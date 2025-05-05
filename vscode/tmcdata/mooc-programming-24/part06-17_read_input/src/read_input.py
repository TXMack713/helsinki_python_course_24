# Write your solution here
def read_input(text: str, lower_boundary: int, upper_boundary: int):
    
    while True:
        try:
            entry = input(text)
            if int(entry) >= lower_boundary and int(entry) <= upper_boundary:
                return int(entry)
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_boundary} and {upper_boundary}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
