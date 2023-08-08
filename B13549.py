from collections import deque

N, K = map(int, input().split())

queue = deque()
visited = [0] * 200001

while N <= 200000:

    visited[N] = 1
    queue.append(N)

    N *= 2

    if not N:
        break

answer = 0
while queue:
    num = queue.popleft()
    step = visited[num]

    if num == K:
        answer = step-1
        break
    
    tmp = 2*num
    while tmp <= 200000:

        if not tmp:
            break

        if visited[tmp] and visited[tmp] <= step:
            break

        if tmp == K:
            answer = step-1
            break

        visited[tmp] = step
        queue.append(tmp)
        tmp *= 2

    if answer:
        break

    for next in [num+1, num-1]:

        if 0 <= next < 200001 and not visited[next]:            
            visited[next] = step + 1
            queue.append(next)
    
    if answer:
        break

print(answer)