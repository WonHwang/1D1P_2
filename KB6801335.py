from collections import deque

N, K = map(int, input().split())

answer = []
queue = deque()

for i in range(1, N+1):
    queue.append(i)

cnt = 0
while queue:
    cnt += 1

    if cnt == K:
        answer.append(queue.popleft())
        cnt = 0
        continue
    
    queue.append(queue.popleft())

print("<", end="")
print(*answer, sep=", ", end="")
print(">")