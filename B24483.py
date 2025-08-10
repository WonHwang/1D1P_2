import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

cnt = 1
def dfs(node, grid, visited, t, step):

    global cnt

    visited[node] = step
    t[node] = cnt
    cnt += 1

    for x in grid[node]:
        if not visited[x]:
            dfs(x, grid, visited, t, step+1)

N, M, R = map(int, input().rstrip().split())
grid = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    grid[a].append(b)
    grid[b].append(a)

for i in range(1, N+1):
    grid[i].sort()

visited = [0] * (N+1)
t = [0] * (N+1)

dfs(R, grid, visited, t, 1)

answer = 0
for i in range(1, N+1):
    answer += (visited[i]-1) * t[i]
print(answer)