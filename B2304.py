import sys
input = sys.stdin.readline

N = int(input())
warehouse = [0] * 1001
for _ in range(N):
    L, H = map(int, input().split())
    warehouse[L] = H
DP1 = [warehouse[0]] * 1001
DP2 = [warehouse[1000]] * 1001
point = 0
for i in range(1, 1001):
    DP1[i] = max(DP1[i-1], warehouse[i])
    DP2[1000-i] = max(DP2[1001-i], warehouse[1000-i])
answer = 0
for i in range(1, 1001):
    answer += min(DP1[i], DP2[i])
print(answer)