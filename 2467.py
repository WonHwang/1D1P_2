N = int(input())
nums = list(map(int, input().split()))
i, j = 0, N-1

Min = 2000000000
x, y = 0, N-1
while i < j:
    
    if abs(nums[i] + nums[j]) < Min:
        Min = abs(nums[i] + nums[j])
        x, y = i, j
        
    if nums[i] + nums[j] == 0:
        break
    
    elif nums[i] + nums[j] > 0:
        j -= 1
        
    else:
        i += 1

print(nums[x], nums[y])