import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    targets = set(filter(lambda x:nums.count(x) == 6, nums))
    new_nums = [num for num in nums if num in targets]
    answer = dict()
    for i in range(len(new_nums)):
        num = new_nums[i]
        answer[num] = answer.get(num, [])
        answer[num].append(i+1)
    result = []
    for num in answer:
        result.append([num] + answer[num])
    result.sort(key=lambda x:(sum(x[1:5]), x[5]))
    print(result[0][0])