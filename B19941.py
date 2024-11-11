N, K = map(int, input().split())
hp = list(input())
M = len(hp)
visited = [0] * M
answer = 0
for i in range(M):
    if hp[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < M and not visited[j] and hp[j] == 'H':
                visited[j] = 1
                answer += 1
                break

print(answer)