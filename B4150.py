N = int(input())
DP = [0] * 5000
DP[1] = 1
DP[2] = 1
for i in range(3, 5000):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N])