import sys
input = sys.stdin.readline

N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))

res = [0] * (N+1)
for i in range(N):
    time = costs[i][0]
    cost = costs[i][1]

    if i+time <= N:
        res[i+time] = max(res[i]+cost, res[i+time])
    if i+1 <= N:
        res[i+1] = max(res[i+1], res[i])

print(max(res))