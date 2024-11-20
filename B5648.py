import sys
input = sys.stdin.readline

first_line = list(map(int, input().rstrip().split()))
N = first_line[0]
nums = []
for i in range(1, len(first_line)):
    nums.append(int(str(first_line[i])[::-1]))
while len(nums) < N:
    line = list(map(str, input().rstrip().split()))
    for num in line:
        nums.append(int(num[::-1]))
nums.sort()
for num in nums:
    print(num)