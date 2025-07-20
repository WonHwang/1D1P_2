import sys
from heapq import heappop, heappush
from collections import deque
input = sys.stdin.readline
INF = 10**6

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
grid = [dict() for _ in range(n)]
for _ in range(r):
    a, b, d = map(int, input().split())
    grid[a-1][b-1] = d
    grid[b-1][a-1] = d
for i in range(n):
    grid[i][i] = 0

answer = 0
distances = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    start = i
    heap = []
    distance = distances[i]
    distance[start] = 0
    heappush(heap, (start, 0))
    
    while heap:
        node = heappop(heap)
        now, n_dis = node[0], node[1]
        
        for node in grid[now]:
            tmp = n_dis + grid[now][node]
            if tmp < distance[node]:
                distance[node] = tmp
                heappush(heap, (node, tmp))
    
    count = 0
    for i in range(n):
        if distance[i] <= r:
            count += items[i]
    
    if answer < count:
        answer = count

print(answer)