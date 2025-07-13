# Write your solution here
import random

def roll(die: str):
    a = [3,3,3,3,3,6]
    b = [2,2,2,5,5,5]
    c = [1,4,4,4,4,4]
    if die == "A":
        result = random.sample(a, 1)
    elif die == "B":
        result = random.sample(b, 1)
    elif die == "C":
        result = random.sample(c, 1)
    else:
        print("Invalid entry")
        result = None
        # entry = input("Please enter a die: ")
        # roll(entry)
    
    return result[0]

def play(die1: str, die2: str, times: int):
    won1 = 0
    won2 = 0
    tie = 0
    # count = 0
    while won1 + won2 + tie < times:
        if roll(die1) > roll(die2):
            won1 += 1
        elif roll(die1) < roll(die2):
            won2 += 1
        elif roll(die1) == roll(die2):
            tie += 1
        elif roll(die1) is None or roll(die2) is None:
            print("Invalid die rolled. Skipping this round.")
            continue
        # count += 1
        
    
    return (won1, won2, tie)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
    result = play("A", "B", 100)
    print(result)
