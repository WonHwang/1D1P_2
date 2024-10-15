import sys
input = sys.stdin.readline
size = 1000001
rest = 1000000009
DP = [0] * size
DP[1] = 1
DP[2] = 1
DP[3] = 1

for i in range(1, size):
    if i+1 < size:
        DP[i+1] += DP[i]
        DP[i+1] %= rest
    if i+2 < size:
        DP[i+2] += DP[i]
        DP[i+2] %= rest
    if i+3 < size:
        DP[i+3] += DP[i]
        DP[i+3] %= rest

T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N])