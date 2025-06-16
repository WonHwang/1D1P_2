mod = 1000000000
dp = [0] * 1000001
dp[1] = 1
for i in range(2, 1000001):
    dp[i] = (dp[i-1] + dp[i-2]) % mod
N = int(input())
if not N:
    print(0)
    print(0)
elif N < 0 and not abs(N)%2:
    print(-1)
    print(dp[abs(N)])
else:
    print(1)
    print(dp[abs(N)])