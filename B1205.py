N, score, P = map(int, input().split())
nums = []
if N:
    nums = list(map(int, input().split()))
s = score-0.5
nums.append(s)
nums.sort(reverse=True)
while len(nums) < P:
    nums.append(-1)
answer = -1
if nums.index(s) < P:
    if score in nums:
        answer = nums.index(score)+1
    else:
        answer = nums.index(s)+1

print(answer)