N = int(input())
nums = list(map(int, input().split()))
dp = [0] * N
dp[0] = nums[0]
for i in range(1, N):
    if nums[i] > nums[i-1]:
        dp[i] = dp[i-1]
    else:
        dp[i] = nums[i]

answer = 0
for i in range(N):
    res = nums[i] - dp[i]
    if res > answer:
        answer = res
print(answer)