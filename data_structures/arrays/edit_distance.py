def calculate_edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    matrix = [0]*(m+1)
    for i in range(m+1):
        matrix[i] = [0]*(n+1)

    for i in range(m+1):
        matrix[i][0] = i
    matrix[0] = [i for i in range(n+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str2[i-1] == str1[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1

    return matrix[m-1][n-1]


# driver function
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        str1, str2 = map(str, input().split())
        print(calculate_edit_distance(str1, str2))
        t -= 1
