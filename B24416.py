# 주어진 수도코드 직접 카운트하면 pypy3에서만 통화 python3 환경에서 시간초과
def fibo(n):
    dp = [1] * n

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n-1]

N = int(input())

print(fibo(N), N-2)