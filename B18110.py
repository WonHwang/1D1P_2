import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num)+1
    return int(num)

nums = []
N = int(input())
for _ in range(N):
    nums.append(int(input()))
nums.sort()
target = my_round(N*0.15)
if target:
    nums = nums[target:-target]
answer = 0
if nums:
    answer = my_round(sum(nums)/len(nums))
print(answer)