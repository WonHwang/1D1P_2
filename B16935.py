import sys
input = sys.stdin.readline

def one(matrix, N, M):

    new = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new[N-1-i][j] = matrix[i][j]
    
    return new, N, M

def two(matrix, N, M):

    new = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new[i][M-1-j] = matrix[i][j]
    
    return new, N, M

def three(matrix, N, M):

    new = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(N):
        for j in range(M):
            new[j][N-1-i] = matrix[i][j]
    
    return new, M, N

def four(matrix, N, M):
    
    new = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(N):
        for j in range(M):
            new[M-1-j][i] = matrix[i][j]
    
    return new, M, N

def five(matrix, N, M):

    new = [[0 for _ in range(M)] for _ in range(N)]
    n, m = N//2, M//2

    for i in range(n):
        for j in range(m):
            new[i][j] = matrix[n+i][j]
            new[i][m+j] = matrix[i][j]
            new[n+i][m+j] = matrix[i][m+j]
            new[n+i][j] = matrix[n+i][m+j]
            
    return new, N, M

def six(matrix, N, M):

    new = [[0 for _ in range(M)] for _ in range(N)]
    n, m = N//2, M//2

    for i in range(n):
        for j in range(m):
            new[i][j] = matrix[i][m+j]
            new[i][m+j] = matrix[n+i][m+j]
            new[n+i][m+j] = matrix[n+i][j]
            new[n+i][j] = matrix[i][j]
    
    return new, N, M

N, M, R = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

R = list(map(int, input().split()))
ops = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six
}
for r in R:
    matrix, N, M = ops.get(r)(matrix, N, M)

for i in range(N):
    print(*matrix[i])