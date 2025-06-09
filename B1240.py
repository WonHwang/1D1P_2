import sys
import heapq
input = sys.stdin.readline
INF = 10**9

N, M = map(int, input().split())
grid = [dict() for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    grid[a][b] = d
    grid[b][a] = d

for i in range(1, N+1):
    grid[i][i] = 0

distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    heap = []
    distance[i][i] = 0
    heapq.heappush(heap, [0, i])

    while heap:
        node = heapq.heappop(heap)
        d, now = node[0], node[1]
        
        for node in grid[now]:
            if distance[i][node] > d + grid[now][node]:
                distance[i][node] = d + grid[now][node]
                heapq.heappush(heap, [distance[i][node], node])

for i in range(M):
    a, b = map(int, input().split())
    print(distance[a][b])