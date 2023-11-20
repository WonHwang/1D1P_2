from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sx -= 1
sy -= 1
sd -= 1
ex -= 1
ey -= 1
ed -= 1

visited = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append([sx, sy, sd])
visited[sx][sy][sd] = 1

while queue:
    node = queue.popleft()
    a, b, d = node[0], node[1], node[2]
    step = visited[a][b][d]
    if a == ex and b == ey and d == ed:
        break
    
    if d in [0, 1]:
        di = 2
        if not visited[a][b][di]:
            visited[a][b][di] = step+1
            queue.append([a, b, di])
        
        di = 3
        if not visited[a][b][di]:
            visited[a][b][di] = step+1
            queue.append([a, b, di])
            
    else:
        di = 0
        if not visited[a][b][di]:
            visited[a][b][di] = step+1
            queue.append([a, b, di])
        
        di = 1
        if not visited[a][b][di]:
            visited[a][b][di] = step+1
            queue.append([a, b, di])
    
    for k in range(1, 4):
        x, y = a + k*dx[d], b + k*dy[d]
        if 0 <= x < N and 0 <= y < M and not visited[x][y][d]:
            if grid[x][y]:
                break
            visited[x][y][d] = step+1
            queue.append([x, y, d])

print(visited[ex][ey][ed]-1)
