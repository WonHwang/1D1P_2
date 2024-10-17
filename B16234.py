from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, grid, visited, N, L, R, div):

    queue = deque()
    visited[x][y] = div
    queue.append([x, y])

    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]
        value = grid[a][b]

        for i in range(4):
            x, y = a + dx[i], b + dy[i]

            if 0 <= x < N and 0 <= y < N and not visited[x][y] and L <= abs(grid[x][y] - value) <= R:
                visited[x][y] = div
                queue.append([x, y])

def separate(grid, visited, N):

    Max = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] > Max:
                Max = visited[i][j]
    
    for t in range(1, Max+1):
        grids = []
        Sum = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == t:
                    grids.append([i, j])
                    Sum += grid[i][j]
        
        Sum //= len(grids)
        for g in grids:
            x, y = g[0], g[1]
            grid[x][y] = Sum

N, L, R = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

answer = 0
while True:
    flag = False

    visited = [[0 for _ in range(N)] for _ in range(N)]
    division = 1

    for i in range(N):
        for j in range(N):
            if j+1 < N and L <= abs(grid[i][j] - grid[i][j+1]) <= R and not visited[i][j]:
                flag = True
                bfs(i, j, grid, visited, N, L, R, division)
                division += 1

            if i+1 < N and L <= abs(grid[i][j] - grid[i+1][j]) <= R and not visited[i][j]:
                flag = True
                bfs(i, j, grid, visited, N, L, R, division)
                division += 1
    
    separate(grid, visited, N)
    
    if not flag:
        break

    answer += 1

print(answer)
