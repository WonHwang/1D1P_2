import sys
sys.setrecursionlimit(10**9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]

answer = 0
def dfs(x, y):
    
    global answer
    
    if x == N-1 and y == M-1:
        answer += 1
        return 1
    
    cnt = 0
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < M and grid[a][b] < grid[x][y]:
            if not visited[a][b]:
                res = dfs(a, b)
                if res:
                    cnt += res
                    visited[a][b] = res
                else:
                    visited[a][b] = -1
            elif visited[a][b] > 0:
                cnt += visited[a][b]
                answer += visited[a][b]
    visited[x][y] += cnt
    
    return cnt
                        
dfs(0, 0)
print(answer)