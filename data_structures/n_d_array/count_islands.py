def is_safe(arr, i, j, n, m, visited):
    return 0 <= i < n and 0 <= j < m and not visited[i][j] and arr[i][j]


def DFS(arr, i, j, n, m, visited):
    row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[i][j] = True

    for k in range(8):
        if is_safe(arr, i+row_nbr[k], j+col_nbr[k], n, m, visited):
            DFS(arr, i+row_nbr[k], j+col_nbr[k], n, m, visited)


def findIslands(arr, n, m):
    island_count = 0
    visited = [[False]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                DFS(arr, i, j, n, m, visited)
                island_count += 1

    return island_count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])] for j in range(n[0])]
        c = 0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c += 1
        print(findIslands(matrix, n[0], n[1]))
