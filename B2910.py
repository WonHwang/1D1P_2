N, C = map(int, input().split())
nums = list(map(int, input().split()))
nums_dict = {}
for num in nums:
    nums_dict[num] = nums_dict.get(num, 0) + 1

res = []
for num in nums_dict:
    res.append([num, nums_dict.get(num)])
    
res.sort(key=lambda x:x[1], reverse=True)
for num in res:
    for _ in range(num[1]):
        print(num[0], end=" ")
print()