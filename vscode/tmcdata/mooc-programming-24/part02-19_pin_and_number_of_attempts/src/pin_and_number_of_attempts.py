# Write your solution here
attempts = 0
code = input("PIN: ")

while True:
    if code == "4321":
        result = True
        attempts += 1
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {attempts} attempts")
            break
    else:
        result = False
        attempts += 1
        print("Wrong")
        code = input("PIN: ")
    
