N = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = 0
for i in range(N):
    start, end = 0, N-1
    while start < end:
        res = nums[start] + nums[end]
        if res > nums[i]:
            end -= 1
        
        elif res < nums[i]:
            start += 1
        
        elif res == nums[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break

print(answer)