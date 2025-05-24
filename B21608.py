import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
info = []
for _ in range(N*N):
    info.append(list(map(int, input().split())))

grid = [[0 for _ in range(N)] for _ in range(N)]
friends = dict()

for s in info:
    student = s[0]
    friends[student] = list(s[1:])
    
    cands = []
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                cand = [0, 0, i, j]
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    
                    if 0 <= x < N and 0 <= y < N:
                        if grid[x][y] in friends[student]:
                            cand[0] += 1
                        elif not grid[x][y]:
                            cand[1] += 1
                cands.append(cand)
    
    cands.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    x, y = cands[0][2], cands[0][3]
    grid[x][y] = student

answer = 0
scores = [0, 1, 10, 100, 1000]
for i in range(N):
    for j in range(N):
        student = grid[i][j]
        cnt = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            
            if 0 <= x < N and 0 <= y < N and grid[x][y] in friends[student]:
                cnt += 1
        answer += scores[cnt]

print(answer)