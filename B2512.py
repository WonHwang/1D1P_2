N = int(input())
nums = list(map(int, input().split()))
limit = int(input())

left, right = 0, max(nums)

while left <= right:
    mid = (left + right) // 2
    
    tmp = 0
    for num in nums:
        if num <= mid:
            tmp += num
        else:
            tmp += mid
    
    if tmp > limit:
        right = mid - 1
    
    else:
        left = mid + 1

tmp = 0
for num in nums:
    if num <= mid:
        tmp += num
    else:
        tmp += mid

if tmp > limit:
    mid -= 1

print(mid)
