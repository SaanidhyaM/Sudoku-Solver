def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None,None
def is_valid(puzzle,guess,row,col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    row_start = (row//3)*3
    col_start = (col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    row,col = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1
    return False
if __name__ == '__main__':
    example_board = [
        [-1, -1, -1,    3,  9, -1,    8,  6, -1],
        [ 1, -1, -1,    5, -1, -1,    7, -1,  9],
        [-1, -1, -1,   -1, -1, -1,   -1,  5, -1],

        [-1, -1,  6,   -1, -1, -1,    2, -1, -1],
        [ 2, -1,  4,   -1,  7, -1,    1, -1,  3],
        [-1, -1,  7,   -1, -1, -1,    4, -1, -1],

        [-1,  7, -1,   -1, -1, -1,   -1, -1, -1],
        [ 4, -1,  2,   -1, -1,  3,   -1, -1,  8],
        [-1,  5,  9,   -1,  8,  4,   -1, -1, -1],
    ]
    print("Sudoku Problem:- \n")
    for i in range(0,9):
        for j in range(0,9):
            if example_board[i][j] == -1:
                print("_", end=' ')
            else:
                print(example_board[i][j], end=' ')
            if j == 2:
                print('\t\t', end='')
            if j == 5:
                print('\t\t', end='')
        print('\n')
        if i == 2 or i == 5:
            print('\n')
    if solve_sudoku(example_board):
        print("*"*50)
        print("SOLVABLE \nThe solution:-\n")
    else:
        print("*"*50)
        print("UNSOLVABLE\n")
    for i in range(0,9):
        for j in range(0,9):
            if example_board[i][j] == -1:
                print(0, end=' ')
                continue
            print(example_board[i][j], end=' ')
            if j == 2:
                print('\t\t', end='')
            if j == 5:
                print('\t\t', end='')
        print('\n')
        if i == 2 or i == 5:
            print('\n')