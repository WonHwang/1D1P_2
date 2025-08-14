N, K = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for last in range(N-1, 0, -1):
    Max = nums[0]
    idx = 0
    for i in range(last+1):
        if nums[i] > Max:
            Max = nums[i]
            idx = i
    
    if idx != last:
        nums[idx], nums[last] = nums[last], nums[idx]
        cnt += 1

    if cnt == K:
        break

if cnt == K:
    print(*nums)
else:
    print(-1)