from collections import deque

A, B, C = map(int, input().split())

a, b, c = 0, 0, C
queue = deque()
queue.append([a, b, c])
visited =[[[0 for _ in range(201)] for _ in range(201)] for _ in range(201)]
visited[a][b][c] = 1

answer = []

while queue:
    node = queue.popleft()
    a, b, c = node[0], node[1], node[2]
    if not a:
        answer.append(c)
    
    # A -> B
    x = max(a - (B-b), 0)
    y = b + (a-x)
    z = c
    if 0 <= x <= 200 and 0 <= y <= 200 and 0 <= z <= 200 and not visited[x][y][z]:
        visited[x][y][z] = 1
        queue.append([x, y, z])
    
    # A -> C
    x = max(a - (C-c), 0)
    y = b
    z = c + (a-x)
    if 0 <= x <= 200 and 0 <= y <= 200 and 0 <= z <= 200 and not visited[x][y][z]:
        visited[x][y][z] = 1
        queue.append([x, y, z])
        
    # B -> A
    y = max(b - (A-a), 0)
    x = a + (b-y)
    z = c
    if 0 <= x <= 200 and 0 <= y <= 200 and 0 <= z <= 200 and not visited[x][y][z]:
        visited[x][y][z] = 1
        queue.append([x, y, z])
        
    # B -> C
    y = max(b - (C-c), 0)
    x = a
    z = c + (b-y)
    if 0 <= x <= 200 and 0 <= y <= 200 and 0 <= z <= 200 and not visited[x][y][z]:
        visited[x][y][z] = 1
        queue.append([x, y, z])
        
    # C -> A
    z = max(c - (A-a), 0)
    y = b
    x = a + (c-z)
    if 0 <= x <= 200 and 0 <= y <= 200 and 0 <= z <= 200 and not visited[x][y][z]:
        visited[x][y][z] = 1
        queue.append([x, y, z])
        
    # C -> B
    z = max(c - (B-b), 0)
    y = b + (c-z)
    x = a
    if 0 <= x <= 200 and 0 <= y <= 200 and 0 <= z <= 200 and not visited[x][y][z]:
        visited[x][y][z] = 1
        queue.append([x, y, z])

answer.sort()
print(*answer)