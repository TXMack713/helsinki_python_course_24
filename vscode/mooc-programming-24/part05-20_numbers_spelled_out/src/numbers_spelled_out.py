# Write your solution here
def dict_of_numbers():
    numbers = {}
    singles = { 0: "zero",
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine"
    }
    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    for x in range(100):
        if x < 10:
            numbers[x] = singles[x]
        elif x >= 10 and x < 20:
            numbers[x] = teens[x]
        elif x > 0 and x % 10 == 0:
            numbers[x] = tens[x]
        elif x > 19 and x % 10 != 0:
            y = x // 10
            y *= 10
            z = int(x % y)
            numbers[x] = tens[y] + "-" + singles[z]
    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])