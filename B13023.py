import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rel = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

answer = 0
visited = [0] * N

def dfs(x, cnt):

    global answer

    if answer:
        return

    if cnt == 5:
        answer = 1
        return

    for friend in rel[x]:
        if not visited[friend]:
            visited[friend] = 1
            dfs(friend, cnt+1)
            visited[friend] = 0

for i in range(N):
    visited[i] = 1
    dfs(i, 1)
    visited[i] = 0

print(answer)