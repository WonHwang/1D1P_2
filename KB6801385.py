N = int(input())
visited = [0] * N

def dfs(step, N, result):

    if step == N:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(i+1)
            dfs(step+1, N, result)
            result.pop()
            visited[i] = 0

dfs(0, N, [])
