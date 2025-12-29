def is_valid(board, row, col, num):
    # چک سطر
    for x in range(9):
        if board[row][x] == num:
            return False

    # چک ستون
    for x in range(9):
        if board[x][col] == num:
            return False

    # چک مربع 3×3
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True