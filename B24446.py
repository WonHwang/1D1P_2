import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
grid = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)

visited = [0] * (N+1)
visited[R] = 1
queue = deque()
queue.append(R)

while queue:
    node = queue.popleft()
    step = visited[node]

    for x in grid[node]:
        if not visited[x]:
            visited[x] = step+1
            queue.append(x)

for i in range(1, N+1):
    print(visited[i]-1 if visited[i] else -1)