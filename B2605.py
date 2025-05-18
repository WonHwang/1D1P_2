from collections import deque

N = int(input())
nums = list(map(int, input().split()))

queue = deque()
for i in range(N):
    target = i+1
    size = len(queue)+1
    for j in range(size):
        if j == nums[i]:
            queue.appendleft(target)
        queue.append(queue.popleft())
print(*list(queue)[::-1])