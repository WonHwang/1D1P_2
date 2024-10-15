from collections import deque

N, K = map(int, input().split())
M = 200001

queue = deque()
visited = dict()
visited[N] = N
queue.append(N)

while queue:
    node = queue.popleft()
    
    if node == K:
        break
    
    x = node + 1
    if 0 <= x < M and visited.get(x) == None:
        visited[x] = node
        queue.append(x)
        
    x = node - 1
    if 0 <= x < M and visited.get(x) == None:
        visited[x] = node
        queue.append(x)
        
    x = 2 * node
    if 0 <= x < M and visited.get(x) == None:
        visited[x] = node
        queue.append(x)

answer = [K]
while True:
    node = visited[answer[-1]]
    if node == N:
        break
    answer.append(node)
answer.append(N)

if N == K:
    print(0)
    print(N)
else:
    print(len(answer)-1)
    print(*answer[::-1])
