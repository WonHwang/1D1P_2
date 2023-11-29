def solution(n):
    dp = [0] * 11
    dp[1] = 1
    for i in range(2, 11):
        dp[i] = i*dp[i-1]
    for i in range(1, 11):
        if dp[i] == n:
            answer = i
            break
        elif dp[i-1] < n < dp[i]:
            answer = i-1
            break
    return answer
