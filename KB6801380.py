from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M, K = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    grid[a-1][b-1] = 1

queue = deque()
visited = [[0 for _ in range(M)] for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = 1
            queue.append([i, j])
            
            cnt = 0
            while queue:
                node = queue.popleft()
                cnt += 1
                a, b = node[0], node[1]

                for k in range(4):
                    x, y = a + dx[k], b + dy[k]
                    if 0 <= x < N and 0 <= y < M and not visited[x][y] and grid[x][y]:
                        visited[x][y] = 1
                        queue.append([x, y])
            
            if cnt > answer:
                answer = cnt

print(answer)
