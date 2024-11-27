import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))[::-1]
    DP = [nums[0]] * N
    answer = 0
    for i in range(1, N):
        if DP[i] < nums[i]:
            DP[i] = nums[i]
        if DP[i-1] > DP[i]:
            DP[i] = DP[i-1]
        answer += abs(nums[i] - DP[i])
    print(answer)