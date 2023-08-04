N, L = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

answer = 0

for i in range(N):
    visited = [0] * N
    flag = 1
    for j in range(N-1):
        if grid[i][j+1] > grid[i][j]:
            if grid[i][j+1] - grid[i][j] > 1:
                flag = 0
                break
            
            cnt = 0
            for k in range(j, max(j-L, -1), -1):
                if not visited[k] and grid[i][k] == grid[i][j]:
                    cnt += 1
                
                if cnt == L:
                    break

            if cnt != L:
                flag = 0
                break

            else:
                for k in range(j, j-L, -1):
                    visited[k] = 1
        
        if grid[i][j+1] < grid[i][j]:
            if grid[i][j] - grid[i][j+1] > 1:
                flag = 0
                break

            cnt = 0
            for k in range(j+1, min(j+1+L, N)):
                if not visited[k] and grid[i][k] == grid[i][j+1]:
                    cnt += 1
                
                if cnt == L:
                    break

            if cnt != L:
                flag = 0
                break

            else:
                for k in range(j+1, j+1+L):
                    visited[k] = 1

    if flag:
        answer += 1

for j in range(N):
    visited = [0] * N
    flag = 1
    for i in range(N-1):
        if grid[i+1][j] > grid[i][j]:
            if grid[i+1][j] - grid[i][j] > 1:
                flag = 0
                break
            
            cnt = 0
            for k in range(i, max(i-L, -1), -1):
                if not visited[k] and grid[k][j] == grid[i][j]:
                    cnt += 1
                
                if cnt == L:
                    break
            
            if cnt != L:
                flag = 0
                break

            else:
                for k in range(i, i-L, -1):
                    visited[k] = 1

        if grid[i+1][j] < grid[i][j]:
            if grid[i][j] - grid[i+1][j] > 1:
                flag = 0
                break

            cnt = 0
            for k in range(i+1, min(i+1+L, N)):
                if not visited[k] and grid[k][j] == grid[i+1][j]:
                    cnt += 1
                
                if cnt == L:
                    break
            
            if cnt != L:
                flag = 0
                break

            else:
                for k in range(i+1, i+1+L):
                    visited[k] = 1
                
    if flag:
        answer += 1

print(answer)