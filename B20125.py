import sys
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

center = []
for i in range(N):
    for j in range(N):
        if 0 < i < N-1 and 0 < j < N-1 and grid[i][j] == grid[i+1][j] == grid[i][j+1] == grid[i-1][j] == grid[i][j-1] == '*':
            center = [i, j]
            break
    if center:
        break

answer = []
cnt = 0
for j in range(center[1]):
    if grid[center[0]][j] == '*':
        cnt += 1
answer.append(cnt)

cnt = 0
for j in range(center[1]+1, N):
    if grid[center[0]][j] == '*':
        cnt += 1
answer.append(cnt)

cnt = 0
for i in range(center[0]+1, N):
    if grid[i][center[1]] == '*':
        cnt += 1
answer.append(cnt)

cnt = 0
for i in range(center[0]+1, N):
    if grid[i][center[1]-1] == '*':
        cnt += 1
answer.append(cnt)

cnt = 0
for i in range(center[0]+1, N):
    if grid[i][center[1]+1] == '*':
        cnt += 1
answer.append(cnt)

center[0] += 1
center[1] += 1
print(*center)
print(*answer)