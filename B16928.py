from collections import deque

N, M = map(int, input().split())

grid = [i for i in range(101)]
visited = [0] * 101
info = [[] for _ in range(101)]

for _ in range(N+M):
    a, b = map(int, input().split())
    info[a].append(b)

queue = deque()
queue.append(1)
visited[1] = 1
step = 0

while queue:
    node = queue.popleft()
    step = visited[node]

    if node == 100:
        break

    for i in range(1, 7):
        x = node + i

        if x < 101 and not visited[x]:

            if info[x]:
                if not visited[info[x][0]]:
                    visited[info[x][0]] = step+1
                    queue.append(info[x][0])
            else:
                visited[x] = step+1
                queue.append(x)


print(visited[100]-1)