N = int(input())
M = int(input())
nums = list(map(int, input().split()))
nums.sort()
left, right = 0, N-1
answer = 0
while left < right:
    Sum = nums[left] + nums[right]
    if Sum == M:
        answer += 1
        left += 1
        right -= 1
    
    elif Sum > M:
        right -= 1
    
    else:
        left += 1

print(answer)