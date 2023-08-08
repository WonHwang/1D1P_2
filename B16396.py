N = int(input())
grid = [0] * 10001
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, b):
        grid[i] = 1

answer = 0
for i in range(10001):
    if grid[i]:
        answer += 1

print(answer)