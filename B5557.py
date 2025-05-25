N = int(input())
nums = list(map(int, input().split()))[::-1]
DP = [dict() for _ in range(N)]
DP[0][nums[0]] = 1
for i in range(1, N):
    num = nums[i]
    for target in DP[i-1]:
        cnt = DP[i-1][target]
        if target + num <= 20:
            DP[i][target+num] = DP[i].get(target+num, 0) + cnt
        if target - num >= 0:
            DP[i][target-num] = DP[i].get(target-num, 0) + cnt

if DP[N-2].get(nums[N-1]):
    print(DP[N-2][nums[N-1]])
else:
    print(0)