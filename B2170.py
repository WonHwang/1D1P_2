import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))
nums.sort(key=lambda x:(x[0], x[1]))

answer = 0
Max = -1000000001
for num in nums:
    a, b = num[0], num[1]
    if a >= Max:
        answer += b-a
        Max = b
    else:
        if b > Max:
            answer += b-Max
            Max = b

print(answer)