N = int(input())
answer = []
for i in range(1, N+1):
    nums = [N, i]
    while True:
        if nums[-1] < 0:
            nums.pop()
            break
        nums.append(nums[-2] - nums[-1])
    
    if len(nums) > len(answer):
        answer = nums[::]
print(len(answer))
print(*answer)