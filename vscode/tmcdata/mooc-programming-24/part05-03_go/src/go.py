# Write your solution here
def who_won(game_board: list):
    zero = 0
    one = 0
    two = 0
    for x in game_board:
        for y in x:
            if y == 0:
                zero += 1
            elif y == 1:
                one += 1
            elif y == 2:
                two += 1
    if one > two:
        return 1
    elif two > one:
        return 2
    elif one == two:
        return 0

if __name__ == "__main__":
    matrix = [[1,2,0,1,2,0,0,1,1,1], [0,2,2,0,1,2,1,1,2,2]]
    who_won(matrix)