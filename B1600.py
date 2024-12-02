import sys
from collections import deque
input = sys.stdin.readline

dx = [2, 2, -2, -2, 1, -1, 1, -1, 1, -1, 0, 0]
dy = [1, -1, 1, -1, 2, -2, -2, 2, 0, 0, 1, -1]

K = int(input())
W, H = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(list(map(int, input().split())))

visited = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
visited[0][0][K] = 1
queue = deque()
queue.append([0, 0, K])
answer = 0

while queue:
    node = queue.popleft()
    a, b, left = node[0], node[1], node[2]
    step = visited[a][b][left]

    if a == H-1 and b == W-1:
        answer = step
        break

    for i in range(12):
        x, y = a + dx[i], b + dy[i]
        if i < 8:
            if left and 0 <= x < H and 0 <= y < W and not grid[x][y] and not visited[x][y][left-1]:
                visited[x][y][left-1] = step+1
                queue.append([x, y, left-1])
        else:
            if 0 <= x < H and 0 <= y < W and not grid[x][y] and not visited[x][y][left]:
                visited[x][y][left] = step+1
                queue.append([x, y, left])

print(answer-1)