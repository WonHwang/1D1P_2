from collections import deque
N = int(input())
queue = deque()
isqueue = list(map(int, input().split()))
values = list(map(int, input().split()))

for i in range(N-1, -1, -1):
    if not isqueue[i]:
        queue.append(values[i])

M = int(input())
values = list(map(int, input().split()))
answer = []
for value in values:
    queue.append(value)
    answer.append(queue.popleft())

print(*answer)