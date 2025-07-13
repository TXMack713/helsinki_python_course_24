# Write your solution here
import fractions

def fractionate(amount: int):
    nums = []
    count = 0
    while count < amount:
        nums.append(fractions.Fraction(1,amount))
        count += 1
    return nums

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    
    print()
