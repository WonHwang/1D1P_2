import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

queue = deque()

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'F':
            queue.append(['F', i, j, 0])
visited = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'J':
            queue.append(['J', i, j, 0])
            visited[i][j] = 0

answer = 0
while queue:
    node = queue.popleft()
    dst, a, b, step = node[0], node[1], node[2], node[3]
    
    if dst == 'J' and (a in (0, N-1) or b in (0, M-1)):
        answer = step+1
        break
    
    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        if 0 <= x < N and 0 <= y < M and grid[x][y] == '.':
            if dst == 'F':
                grid[x][y] = 'F'
                queue.append(['F', x, y, step+1])
            if dst == 'J' and visited[x][y] == -1:
                visited[x][y] = step+1
                queue.append(['J', x, y, step+1])

print(answer if answer else 'IMPOSSIBLE')