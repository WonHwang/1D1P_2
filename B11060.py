from collections import deque

N = int(input())
nums = list(map(int, input().split()))

queue = deque()
queue.append(0)
visited = [0] * N
visited[0] = 1

while queue:
    idx = queue.popleft()
    step = visited[idx]

    if idx == N-1:
        break

    for i in range(nums[idx], 0, -1):
        x = idx + i
        if x < N and not visited[x]:
            visited[x] = step+1
            queue.append(x)

print(visited[N-1]-1)