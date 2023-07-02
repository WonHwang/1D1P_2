import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().rstrip().split())))

prefix = [[0 for _ in range(M)] for _ in range(N)]

prefix[0][0] = grid[0][0]
for i in range(1, N):
    prefix[i][0] = grid[i][0] + prefix[i-1][0]
for j in range(1, M):
    prefix[0][j] = grid[0][j] + prefix[0][j-1]

for i in range(1, N):
    for j in range(1, M):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i][j]

K = int(input().rstrip())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    if x1 == 0 and y1 == 0:
        print(prefix[x2][y2])
    
    elif x1 == 0 and y1 != 0:
        print(prefix[x2][y2] - prefix[x2][y1-1])
    
    elif x1 != 0 and y1 == 0:
        print(prefix[x2][y2] - prefix[x1-1][y2])
    
    else:
        print(prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1])