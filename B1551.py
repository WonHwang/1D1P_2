N, K = map(int, input().split())
nums = list(map(int, input().split(',')))
for _ in range(K):
    tmp = []
    for i in range(len(nums)-1):
        tmp.append(nums[i+1]-nums[i])
    nums = tmp
answer = []
for num in nums:
    answer.append(str(num))
print(','.join(answer))