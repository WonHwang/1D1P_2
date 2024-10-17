from collections import deque

dx = [1, 0, 0]
dy = [0, 1, -1]

H, W = map(int, input().split())
grid = [[0 for _ in range(W)] for _ in range(H)]
visited = [[0 for _ in range(W)] for _ in range(H)]

def bfs(x, y, grid, visited, H, W):

    queue = deque()
    visited[x][y] = 1
    queue.append([x, y])

    while queue:
        node = queue.popleft()

        for i in range(3):
            x, y = node[0] + dx[i], node[1] + dy[i]

            if 0 <= x < H and 0 <= y < W and not visited[x][y] and not grid[x][y]:
                visited[x][y] = 1
                queue.append([x, y])

heights = list(map(int, input().split()))
for j in range(W):
    height = heights[j]
    for i in range(height):
        grid[H-1-i][j] = 1

for i in range(H):
    for j in range(W):
        if grid[i][j]:
            start = j
            end = 0
            for k in range(j+1, W):
                if grid[i][k]:
                    end = k
                    break
            
            if end:
                point = (start + end ) // 2
                if not visited[i][point] and not grid[i][point]:
                    bfs(i, point, grid, visited, H, W)

answer = 0
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            answer += 1

print(answer)