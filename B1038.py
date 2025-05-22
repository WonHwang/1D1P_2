nums = []

def dfs(digit, num):

    global nums

    nums.append(int(num[::-1]))

    for i in range(digit+1, 10):
        dfs(i, num+str(i))

for i in range(10):
    dfs(i, str(i))

nums.sort()
size = len(nums)
N = int(input())
print(nums[N] if N < size else -1)