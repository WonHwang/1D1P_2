import sys
input = sys.stdin.readline

N, D = map(int, input().split())
DP = [i for i in range(10001)]
roads = []
for _ in range(N):
    roads.append(list(map(int, input().split())))
roads.sort(key=lambda x:(x[0], x[1], x[2]))

for road in roads:
    a, b, d = road[0], road[1], road[2]
    DP[b] = min(DP[b], DP[a]+d)
    for i in range(1, 10001):
        DP[i] = min(DP[i-1]+1, DP[i])

print(DP[D])