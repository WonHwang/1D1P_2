N, K = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
answer = []
for last in range(N-1, 0, -1):
    for i in range(last):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            cnt += 1
        if cnt == K:
            answer = nums[::]
            break

    if answer:
        break
    
if answer:
    print(*answer)
else:
    print(-1)