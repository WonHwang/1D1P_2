from collections import deque

N = int(input())
nums = list(map(int, input().split()))

queue = deque()
for i in range(N):
    queue.append([i+1, nums[i]])

answer = []
while queue:
    target = queue.popleft()
    answer.append(target[0])

    num = target[1]

    if num > 0:
        for i in range(num-1):
            if queue:
                queue.append(queue.popleft())
    
    else:
        for i in range(abs(num)):
            if queue:
                queue.appendleft(queue.pop())

print(*answer)