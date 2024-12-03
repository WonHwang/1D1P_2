'''
기존코드 python3=>TLE, pypy3=>pass
visited[1000][1000][11] 보다 visited[11][1000][1000] 이 훨씬 빠름
근데도 실패..
'''

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
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(11)]
queue.append([0, 0, K])
visited[K][0][0] = 1
answer = -1

while queue:
    node = queue.popleft()
    a, b, left = node[0], node[1], node[2]
    step = visited[left][a][b]
    
    if a == N-1 and b == M-1:
        answer = step
        break
    
    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        
        if 0 <= x < N and 0 <= y < M:
            if left > 0 and grid[x][y] == '1' and not visited[left-1][x][y]:
                visited[left-1][x][y] = step+1
                queue.append([x, y, left-1])
            
            elif grid[x][y] == '0' and not visited[left][x][y]:
                visited[left][x][y] = step+1
                queue.append([x, y, left])

print(answer)