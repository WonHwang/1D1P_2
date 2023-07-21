import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
grid = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    grid[a].append(b)
    grid[b].append(a)

for i in range(1, N+1):
    if grid[i]:
        grid[i].sort()
        
visited = [0] * (N+1)
queue = deque()
visited[R] = 1
queue.append(R)
cnt = 2

while queue:
    node = queue.popleft()
    step = visited[node]

    for x in grid[node]:
        if not visited[x]:
            visited[x] = cnt
            cnt += 1
            queue.append(x)

for i in range(1, N+1):
    sys.stdout.write(str(visited[i]) + "\n")