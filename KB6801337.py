from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start, cont, grid, n, m):

    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    visited[start[0]][start[1]] = 1
    queue.append(start)


    for con in cont:
        visited[con[0]][con[1]] = 2
        queue.append(con)

    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]
        dst = visited[a][b]

        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                visited[x][y] = dst
                queue.append([x, y])
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                cnt += 1
    
    return cnt

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))

contaminations = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'x':
            contaminations.append([i, j])

answer = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            start = [i, j]
            cnt = bfs(start, contaminations, grid, n, m)
            if cnt > answer:
                answer = cnt

print(answer)