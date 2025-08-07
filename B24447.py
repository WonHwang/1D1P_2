import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
grid = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)

d = [0] * (N+1)
t = [0] * (N+1)

d[R] = 1
queue = deque()
queue.append(R)
cnt = 1

while queue:
    node = queue.popleft()
    step = d[node]
    t[node] = cnt
    cnt += 1

    for x in grid[node]:
        if not d[x]:
            d[x] = step+1
            queue.append(x)

answer = 0
for i in range(1, N+1):
    answer += t[i] * (d[i]-1)
print(answer)