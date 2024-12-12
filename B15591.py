import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
connections = [dict() for _ in range(N+1)]
for _ in range(N-1):
    a, b, r = map(int, input().split())
    connections[a][b] = r
    connections[b][a] = r

for _ in range(Q):
    k, v = map(int, input().split())

    visited = [0] * (N+1)
    visited[v] = 1

    queue = deque()
    queue.append([v, 10**10])
    
    cnt = 0
    while queue:
        node = queue.popleft()
        x, usa = node[0], node[1]

        for v in connections[x]:
            usa_ = connections[x][v]
            next_usa = min(usa, usa_)
            if not visited[v] and next_usa >= k:
                cnt += 1
                visited[v] = 1
                queue.append([v, next_usa])
    
    print(cnt)

'''
4 3
1 2 3
2 3 2
2 4 4
1 2
4 1
3 1

5 3
1 2 3
2 3 2
2 4 4
3 5 5

'''