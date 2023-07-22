import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M, R = map(int, input().rstrip().split())
grid = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    grid[a].append(b)
    grid[b].append(a)

for i in range(N+1):
    if grid[i]:
        grid[i].sort(reverse=True)

step = 1
visited = [0] * (N+1)
visited[R] = step
step += 1
queue = deque()
queue.append(R)

while queue:
    node = queue.popleft()

    for x in grid[node]:
        if not visited[x]:
            visited[x] = step
            step += 1
            queue.append(x)

for i in range(1, N+1):
    print(str(visited[i]) + '\n')