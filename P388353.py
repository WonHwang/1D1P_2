from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(grid, target):
    N, M = len(grid), len(grid[0])
    
    queue = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    visited[0][0] = 1
    queue.append([0, 0])
    
    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]
        
        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            
            if 0 <= x < N and 0 <= y < M and not visited[x][y] and (grid[x][y] == 0 or grid[x][y] == target):
                if grid[x][y] == 0:
                    visited[x][y] = 1
                    queue.append([x, y])
                
                else:
                    visited[x][y] = 2
                    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 2:
                grid[i][j] = 0

def reduce(grid, target):
    
    N, M = len(grid), len(grid[0])
    for i in range(N):
        for j in range(M):
            if grid[i][j] == target:
                grid[i][j] = 0

def solution(storage, requests):
    answer = 0
    N, M = len(storage), len(storage[0])
    grid = []
    grid.append([0 for _ in range(M+2)])
    for i in range(N):
        grid.append([0] + list(storage[i]) + [0])
    grid.append([0 for _ in range(M+2)])
    
    for request in requests:
        if len(request) == 2:
            reduce(grid, request[0])
        
        else:
            bfs(grid, request)
    
    for i in range(N+2):
        for j in range(M+2):
            if grid[i][j] != 0:
                answer += 1
    
    return answer