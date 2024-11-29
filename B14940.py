import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))
visited = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()
start = []
for i in range(N):
    for j in range(M):
        if nums[i][j] == 2:
            queue.append([i, j])
            break
    if queue:
        break

while queue:
    node = queue.popleft()
    a, b = node[0], node[1]
    step = visited[a][b]

    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        if 0 <= x < N and 0 <= y < M and not visited[x][y] and nums[x][y] == 1:
            visited[x][y] = step+1
            queue.append([x, y])

for i in range(N):
    for j in range(M):
        if nums[i][j] == 1 and not visited[i][j]:
            visited[i][j] = -1

for i in range(N):
    print(*visited[i])