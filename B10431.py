import sys
input = sys.stdin.readline

for _ in range(int(input())):

    nums = list(map(int, input().split()))
    line = []
    answer = 0
    for i in range(1, 21):
        if line:
            for num in line:
                if num > nums[i]:
                    answer += 1
        line.append(nums[i])
    
    print(f"{nums[0]} {answer}")