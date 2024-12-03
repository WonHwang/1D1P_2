import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M, K = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input()))

queue = deque()
visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
queue.append([0, 0, K])
visited[0][0][K] = 1
answer = -1

while queue:
    node = queue.popleft()
    a, b, left = node[0], node[1], node[2]
    step = visited[a][b][left]
    
    if a == N-1 and b == M-1:
        answer = step
        break
    
    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        
        if 0 <= x < N and 0 <= y < M:
            if left > 0 and grid[x][y] == '1' and not visited[x][y][left-1]:
                visited[x][y][left-1] = step+1
                queue.append([x, y, left-1])
            
            elif grid[x][y] == '0' and not visited[x][y][left]:
                visited[x][y][left] = step+1
                queue.append([x, y, left])

print(answer)