# Write your solution here
def transpose(matrix: list):
    new_matrix = []
    length = len(matrix)
    column_counter = 0
    
    while column_counter < length:
        new_row = []
        row_counter = 0
        while row_counter < length:
            new_row.append(matrix[row_counter][column_counter])
            row_counter += 1
        column_counter += 1
        new_matrix.append(new_row)
    
    row_counter = 0
    while row_counter < length:
        column_counter = 0
        while column_counter < length:
            matrix[row_counter][column_counter] = new_matrix[row_counter][column_counter]
            column_counter += 1
        row_counter += 1
    # return matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    transpose(matrix)
    print(matrix)
            
