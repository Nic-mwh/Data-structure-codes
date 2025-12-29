N = 8
board = [[0]*N for _ in range(N)]

def is_safe(row, col):
    # چک سطر
    for i in range(col):
        if board[row][i] == 1:
            return False

    # قطر بالا
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # قطر پایین
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_queens(col):
    if col == N:
        return True

    for row in range(N):
        if is_safe(row, col):
            board[row][col] = 1
            if solve_queens(col + 1):
                return True
            board[row][col] = 0

    return False


solve_queens(0)
for row in board:
    print(row)