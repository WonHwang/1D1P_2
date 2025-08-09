import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, grid, visited, step):

    visited[node] = step

    for x in grid[node]:
        if not visited[x]:
            dfs(x, grid, visited, step+1)

N, M, R = map(int, input().rstrip().split())
grid = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    grid[a].append(b)
    grid[b].append(a)

for i in range(1, N+1):
    grid[i].sort(reverse=True)

visited = [0] * (N+1)

dfs(R, grid, visited, 1)

for x in visited[1:]:
    sys.stdout.write(str(x-1) + '\n')