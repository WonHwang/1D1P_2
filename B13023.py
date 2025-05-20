N, M = map(int, input().split())
rel = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

answer = 0

def dfs(visited, x):

    global answer

    if answer:
        return

    if sum(visited) == 5:
        answer = 1
        return

    for friend in rel[x]:
        if not visited[friend]:
            visited[friend] = 1
            dfs(visited, friend)
            visited[friend] = 0

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    dfs(visited, i)

print(answer)