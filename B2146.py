from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

cnt = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] and not visited[i][j]:
            cnt += 1
            queue = deque()
            queue.append([i, j])
            visited[i][j] = cnt
            
            while queue:
                node = queue.popleft()
                a, b = node[0], node[1]
                
                for k in range(4):
                    x, y = a + dx[k], b + dy[k]
                    if 0 <= x < N and 0 <= y < N and grid[x][y] and not visited[x][y]:
                        visited[x][y] = cnt
                        queue.append([x, y])

Min = N*N
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            flag = 0
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < N and 0 <= y < N and not grid[x][y]:
                    flag = 1
                    break
            if flag:
                queue = deque()
                queue.append([i, j])
                visit = [[0 for _ in range(N)] for _ in range(N)]
                visit[i][j] = 1
                start = visited[i][j]
                res = 0
                
                while queue:
                    node = queue.popleft()
                    a, b = node[0], node[1]
                    step = visit[a][b]
                    
                    for k in range(4):
                        x, y = a + dx[k], b + dy[k]
                        if 0 <= x < N and  0 <= y < N:
                            if grid[x][y] and visited[x][y] != start:
                                res = step
                                break
                            if not grid[x][y] and not visit[x][y]:
                                visit[x][y] = step+1
                                queue.append([x, y])
                    
                    if res:
                        break
                if res and res < Min:
                    Min = res

print(Min-1)