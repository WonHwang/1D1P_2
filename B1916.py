import sys
input = sys.stdin.readline
INF = 10**9

V = int(input())
E = int(input())
grid = dict()
for _ in range(E):
    a, b, d = map(int, input().split())
    if grid.get(a):
        if grid[a].get(b) != None:
            grid[a][b] = min(grid[a][b], d)
        else:
            grid[a][b] = d
    
    else:
        grid[a] = dict()
        grid[a][b] = d

for i in range(1, V+1):
    if grid.get(i):
        grid[i][i] = 0
    else:
        grid[i] = dict()
        grid[i][i] = 0

S, D = map(int, input().split())

distance = [INF] * (V+1)
distance[S] = 0
visited = [0] * (V+1)
now = S

while now > 0:
    for node in grid[now]:
        distance[node] = min(distance[now] + grid[now][node], distance[node])
    visited[now] = 1
    now = -1
    tmp = INF
    for i in range(1, V+1):
        if not visited[i] and distance[i] < tmp:
            now = i
            tmp = distance[i]

print(distance[D])