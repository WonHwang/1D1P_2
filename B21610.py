import sys
input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

ddx = [1, 1, -1, -1]
ddy = [1, -1, 1, -1]

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

orders = []
for _ in range(M):
    orders.append(list(map(int, input().split())))

def move_and_rain_and_watercopybug_and_newclouds(clouds, order):

    res = []
    direction, cnt = order[0]-1, order[1]
    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        x = x + cnt * dx[direction]
        y = y + cnt * dy[direction]
        x %= N
        y %= N
        res.append([x, y])
    
    clouds = res

    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        grid[x][y] += 1
    
    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        cnt = 0
        for i in range(4):
            a, b = x + ddx[i], y + ddy[i]
            if 0 <= a < N and 0 <= b < N and grid[a][b]:
                cnt += 1
        grid[x][y] += cnt

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        visited[x][y] = 1
    
    clouds = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] >= 2:
                clouds.append([i, j])
                grid[i][j] -= 2
    
    return clouds

clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for order in orders:
    clouds = move_and_rain_and_watercopybug_and_newclouds(clouds, order)

answer = 0
for i in range(N):
    for j in range(N):
        answer += grid[i][j]

print(answer)