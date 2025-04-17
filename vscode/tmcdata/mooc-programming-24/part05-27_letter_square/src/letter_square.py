# Write your solution here
def square_of_letters():
    num = int(input("Layers: "))
    letters = {
        1: "A",
        2: "B", 
        3: "C", 
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z"
    }
       
    grid = 1
    if num > 1:
        grid = num + (num - 1)
    
    square = []
    for i in range (grid):
        entry = []
        count = 1
        while count <= grid:
            entry.append(letters[num])
            count += 1
        square.append(entry)
    
    current_letter = num - 1
    start_row = 1
    current_row = 0
    end_row = len(square) - 2
    start_index = 1
    current_index = 0
    end_index = grid - 2

    while current_letter >= 1:
        current_row = start_row
        while current_row <= end_row:
            current_index = start_index
            while current_index <= end_index:
                square[current_row][current_index] = letters[current_letter]
                current_index += 1
            current_row += 1
        start_index += 1
        end_index -= 1
        start_row += 1
        end_row -= 1
        current_letter -= 1
    
    for row in square:
        string = ""
        for letter in row:
            string += letter
        print(string)

square_of_letters()