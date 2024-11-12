answer = 0

def dfs(total, x, y, grid, N, M, direction):

    global answer
    if 0 <= x < N and 0 <= y < M:
        
        total += grid[x][y]
        if total > answer:
            return

        if x == N-1:
            if total < answer:
                answer = total
            return
        
        if x == 0:
            dfs(total, x+1, y-1, grid, N, M, 0)
            dfs(total, x+1, y, grid, N, M, 1)
            dfs(total, x+1, y+1, grid, N, M, 2)

        elif direction == 0:
            dfs(total, x+1, y, grid, N, M, 1)
            dfs(total, x+1, y+1, grid, N, M, 2)
        
        elif direction == 1:
            dfs(total, x+1, y-1, grid, N, M, 0)
            dfs(total, x+1, y+1, grid, N, M, 2)
        
        elif direction == 2:
            dfs(total, x+1, y-1, grid, N, M, 0)
            dfs(total, x+1, y, grid, N, M, 1)

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
answer = 10**5
for j in range(M):
    dfs(0, 0, j, grid, N, M, 0)
print(answer)