from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

def findbabyshark():
    
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                return [i, j]

def bfs(x, y, size):
    feed = []
    
    queue = deque()
    queue.append([x, y, 0])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 1
    
    while queue:
        node = queue.popleft()
        x, y, step = node[0], node[1], node[2]
        
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            
            if 0 <= a < N and 0 <= b < N and not visited[a][b]:
                if space[a][b] == 0 or space[a][b] == size:
                    visited[a][b] = 1
                    queue.append([a, b, step+1])
                
                elif 0 < space[a][b] < size:
                    visited[a][b] = 1
                    feed.append([a, b, step+1])
    
    return feed

def selectnextfeed(feed):
    
    step = feed[0][2]
    target = []
    for f in feed:
        if f[2] == step:
            target.append(f)
    
    target_2 = []
    min_x = N
    for t in target:
        if t[0] < min_x:
            min_x = t[0]
    
    for t in target:
        if t[0] == min_x:
            target_2.append(t)
    
    min_y = N
    for t in target_2:
        if t[1] < min_y:
            min_y = t[1]
    
    for t in target_2:
        if t[1] == min_y:
            return t


cnt = 0
size = 2
time = 0

while True:
    
    baby_shark = findbabyshark()
    x, y = baby_shark[0], baby_shark[1]
    
    feed = bfs(x, y, size)
    
    if not feed:
        break
    
    target = selectnextfeed(feed)
    space[x][y] = 0
    space[target[0]][target[1]] = 9
    cnt += 1
    time += target[2]
    if cnt == size:
        cnt = 0
        size += 1

print(time)