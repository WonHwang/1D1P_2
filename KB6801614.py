from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

w, h = map(int, input().split())
grid = []

for _ in range(h):
    grid.append(list(map(int, input().split())))

queue = deque()
visited = [[0 for _ in range(w)] for _ in range(h)]

cnt = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] and not visited[i][j]:
            cnt += 1
            visited[i][j] = 1
            queue.append([i, j])

            while queue:
                node = queue.popleft()
                a, b = node[0], node[1]

                for k in range(8):
                    x, y = a + dx[k], b + dy[k]

                    if 0 <= x < h and 0 <= y < w and not visited[x][y] and grid[x][y]:
                        visited[x][y] = 1
                        queue.append([x, y])

print(cnt)