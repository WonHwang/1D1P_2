from collections import deque

res = [0]
queue = deque()
queue.append(0)
for i in range(1, 10):
    queue.append(i)

while queue:
    num = queue.popleft()
    res.append(num)

    for i in range(num%10):
        queue.append(num*10 + i)

N = int(input())
print(res[N] if N < len(res) else -1)