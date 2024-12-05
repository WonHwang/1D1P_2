N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

answer = 0

def dfs(x, y, dst):

    global answer
    
    if x == N-1 and y == N-1:
        answer += 1
        return

    if dst == 0:
        a, b = x+1, y
        if 0 <= a < N and 0 <= b < N and not grid[a][b]:
            dfs(a, b, 0)
        a, b = x+1, y+1
        if 0 <= a < N and 0 <= b < N and not grid[x][b] and not grid[a][y] and not grid[a][b]:
            dfs(a, b, 1)
    
    elif dst == 1:
        a, b = x+1, y
        if 0 <= a < N and 0 <= b < N and not grid[a][b]:
            dfs(a, b, 0)
        a, b = x+1, y+1
        if 0 <= a < N and 0 <= b < N and not grid[x][b] and not grid[a][y] and not grid[a][b]:
            dfs(a, b, 1)
        a, b = x, y+1
        if 0 <= a < N and 0 <= b < N and not grid[a][b]:
            dfs(a, b, 2)
    
    elif dst == 2:
        a, b = x+1, y+1
        if 0 <= a < N and 0 <= b < N and not grid[x][b] and not grid[a][y] and not grid[a][b]:
            dfs(a, b, 1)
        a, b = x, y+1
        if 0 <= a < N and 0 <= b < N and not grid[a][b]:
            dfs(a, b, 2)

if grid[N-1][N-1] != 1:
    dfs(0, 1, 2)
print(answer)