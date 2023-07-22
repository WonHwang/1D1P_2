import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

step = 1

def dfs(node, grid, visited):

    global step

    visited[node] = step
    step += 1

    for x in grid[node]:
        if not visited[x]:
            dfs(x, grid, visited)

N, M, R = map(int, input().rstrip().split())
grid = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    grid[a].append(b)
    grid[b].append(a)

for i in range(1, N+1):
    grid[i].sort(reverse=True)

visited = [0] * (N+1)

dfs(R, grid, visited)

for x in visited[1:]:
    sys.stdout.write(str(x) + '\n')