import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

points = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            points.append([i, j])

answer = N*N+1
for point in combinations(points, M):
    queue = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for p in point:
        visited[p[0]][p[1]] = 1
        queue.append(p)
    
    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]
        step = visited[a][b]

        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < N and 0 <= y < N and not visited[x][y] and grid[x][y] != 1:
                visited[x][y] = step+1
                queue.append([x, y])
    
    res = step-1
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 1 and not visited[i][j]:
                res = -1
                break
        if res == -1:
            break

    if res != -1 and res < answer:
        answer = res

if answer == N*N+1:
    answer = -1
print(answer)