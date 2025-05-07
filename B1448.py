import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort(reverse=True)

answer = -1
for i in range(N-2):
    if nums[i] < nums[i+1] + nums[i+2]:
        answer = sum(nums[i:i+3])
        break

print(answer)