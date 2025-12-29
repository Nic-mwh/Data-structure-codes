def dfs(matrix, visited, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    if visited[i][j] or matrix[i][j] == 0:
        return

    visited[i][j] = True

    # چهار جهت
    dfs(matrix, visited, i+1, j)
    dfs(matrix, visited, i-1, j)
    dfs(matrix, visited, i, j+1)
    dfs(matrix, visited, i, j-1)


def count_islands(matrix):
    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(matrix, visited, i, j)
                count += 1

    return count


matrix = [
    [1, 1, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1]
]

print(count_islands(matrix))  # خروجی: 3