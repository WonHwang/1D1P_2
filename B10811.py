N, M = map(int, input().split())
arr = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    tmp = []
    for i in range(a, b+1):
        tmp.append(arr[i])
    for i in range(a, b+1):
        arr[i] = tmp.pop()

print(*arr[1:]) 