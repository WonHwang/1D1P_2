from collections import deque

N = int(input())
visited = [[0 for _ in range(10001)] for _ in range(10001)]
queue = deque()
queue.append([1, 0])
visited[1][0] = 1

while queue:
    node = queue.popleft()
    num, board = node[0], node[1]
    time = visited[num][board]

    if num == N:
        print(time-1)
        break
    
    if not visited[num+board][board]:
        visited[num+board][board] = time+1
        queue.append([num + board, board])
    if not visited[num][num]:
        visited[num][num] = time+1
        queue.append([num, num])
    if not visited[num-1][board]:
        visited[num-1][board] = time+1
        queue.append([num-1, board])