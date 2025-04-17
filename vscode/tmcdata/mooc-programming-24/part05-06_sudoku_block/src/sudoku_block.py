# Write your solution here
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
            return False
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))