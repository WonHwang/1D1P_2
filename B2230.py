import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
start, end = 0, 0
answer = nums[-1] - nums[0]
while end < N and start <= end:
    value = nums[end] - nums[start]

    if value >= M:
        if value < answer:
            answer = value
        start += 1
    
    else:
        end += 1
        
print(answer)