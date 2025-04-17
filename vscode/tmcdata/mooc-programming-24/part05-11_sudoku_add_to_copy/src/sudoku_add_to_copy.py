# Write your solution here
def row_correct(sudoku: list, row_no: int):
    nums = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
    for entry in sudoku[row_no]:
        if entry > 0:
            nums[entry] += 1
        for key in nums:
            if nums[key] > 1:
                return False
    return True

def column_correct(sudoku: list, column_no: int):
    nums = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
    for row in sudoku:
        if row[column_no] > 0:
            nums[row[column_no]] += 1
        for key in nums:
            if nums[key] > 1:
                return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    nums = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
    row_limit = row_no + 2
    column_limit = column_no + 2
    row_counter = row_no
    
    while row_counter <= row_limit:
        column_counter = column_no
        while column_counter <= column_limit:
            if sudoku[row_counter][column_counter] > 0:
                nums[sudoku[row_counter][column_counter]] += 1
            column_counter += 1
        row_counter += 1
    
    for key in nums:
        if nums[key] > 1:
            print("Key: " + str(key) + ", value: " + str(nums[key]))
            print("Sudoku")
            print(sudoku)
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    row_count = 0
    column_count = 0
    row_result = True
    column_result = True
    block_result = True
   
    while row_count < 9:
        row_result = row_correct(sudoku, row_count)
        if row_result == False:
            return False
        else:
            row_count += 1
   
    while column_count < 9:
        column_result = column_correct(sudoku, column_count)
        if column_result == False:
            return False
        else:
            column_count += 1
    
    row_count = 0
    
    while row_count < 9:
        column_count = 0
        while column_count < 9:
            block_result = block_correct(sudoku, row_count, column_count)
            if block_result == False:
                print("block result", block_result)
                return False
            else:
                column_count += 3
        row_count += 3
    
    # if row_result == False or column_result == False or block_result == False:
    #     return False
    # else:
    return True

def print_sudoku(sudoku: list):
    grid = sudoku
    row_count = 0
    while row_count < 9:
        column_count = 0
        while column_count < 9:
            if grid[row_count][column_count] == 0:
                grid[row_count][column_count] = "_"
            column_count += 1
        row_count += 1
    
    row_count = 0
    # row_limit = row_count + 2
    
    while row_count < 9:
        if row_count % 3 == 0:
            print("")
        column_count = 0
        string = ""
        while column_count < 9:
            string = string + str(grid[row_count][column_count]) + " "
            if column_count == 2 or column_count == 5:
                string += " "
            column_count += 1
        print(string)
        
        row_count += 1
    
    # print(grid)
    
    # row_limit = row_no + 2
    # column_limit = column_no + 2
    # row_counter = row_no
    
    '''while row_counter <= row_limit:
        column_counter = column_no
        while column_counter <= column_limit:
            if sudoku[row_counter][column_counter] > 0:
                nums[sudoku[row_counter][column_counter]] += 1
            column_counter += 1
        row_counter += 1'''

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    grid = sudoku
    grid[row_no][column_no] = number
    return grid

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid = []
    for row in sudoku:
        new_row = []
        for column in row:
            new_row.append(column)
        grid.append(new_row)
    # print(id(sudoku))
    # print(id(grid))

    grid[row_no][column_no] = number
    return grid

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
