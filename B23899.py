N = int(input())
nums = list(map(int, input().split()))
target = list(map(int, input().split()))

def is_same(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    
    return True

answer = 0
for last in range(N-1, 0, -1):

    if is_same(nums, target):
        answer = 1
        break

    Max = nums[0]
    idx = 0
    for i in range(last+1):
        if nums[i] > Max:
            Max = nums[i]
            idx = i
    
    if idx != last:
        nums[idx], nums[last] = nums[last], nums[idx]
    
    if is_same(nums, target):
        answer = 1
        break
    
print(answer)