from collections import deque
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

def bfs(x, y):
    
    queue = deque()
    visited[x][y] = 1
    queue.append([x, y])
    
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        
        for k in range(4):
            x_, y_ = x + dx[k], y + dy[k]
            if 0 <= x_ < N and 0 <= y_ < M and not visited[x_][y_] and maps[x_][y_]:
                visited[x_][y_] = 1
                queue.append([x_, y_])
    
    return 1

def allMelted():
    for i in range(N):
        for j in range(M):
            if maps[i][j]:
                return False
    
    return True

answer = 0

while True:
    
    divided = 0
    
    if allMelted():
        answer = 0
        break
    
    answer += 1
    
    tmp = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(1, N-1):
        for j in range(1, M-1):
            
            if maps[i][j]:
                cnt = 0
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < N and 0 <= y < M:
                        if maps[x][y] == 0:
                            cnt += 1
                
                tmp[i][j] = max(maps[i][j] - cnt, 0)
    
    maps = copy.deepcopy(tmp)
    
    for i in range(1, N-1):
        for j in range(1, M-1):
            
            if not visited[i][j] and maps[i][j]:
                divided += bfs(i, j)
    
    if divided > 1:
        break  

print(answer)