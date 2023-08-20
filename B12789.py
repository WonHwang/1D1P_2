N = int(input())
nums = list(map(int, input().split()))

nums = nums[::-1]
stack = []

answer = 1
cnt = 1

while nums:

    if nums[-1] == cnt:
        nums.pop()
        cnt += 1
    
    elif stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
    
    else:
        stack.append(nums.pop())

while stack:

    if stack[-1] == cnt:
        stack.pop()
        cnt += 1
    
    else:
        answer = 0
        break

if not answer or cnt != N+1:
    print("Sad")

else:
    print("Nice")