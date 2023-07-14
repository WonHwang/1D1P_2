N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
answer = [0]*M

dic = dict()
for num in nums:
    dic[num] = dic.get(num, 0) + 1

for i in range(M):
    answer[i] = dic.get(targets[i], 0)

print(*answer)