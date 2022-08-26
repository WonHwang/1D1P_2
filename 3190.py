from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

board[0][0] = 2

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
commands = []
for _ in range(L):
    t, d = map(str, input().split())
    t = int(t)
    commands.append([t, d])

commands.append([10001, 'L'])

time = 0
direction = 0
queue = deque()
queue.append([0, 0])
isend = 0

for command in commands:
    point, rotation = command[0], command[1]
    
    while time <= point:
         
        if time == point:
            if rotation == 'L':
                direction = (direction - 1) % 4
        
            elif rotation == 'D':
                direction = (direction + 1) % 4

        front = queue.popleft()
        x, y = front[0], front[1]
        x_ = x + dx[direction]
        y_ = y + dy[direction]
        queue.appendleft(front)
        queue.appendleft([x_, y_])
        
        if not (0 <= x_ < N and 0 <= y_ < N):
            isend = 1
            time += 1
            break
        
        if board[x_][y_] == 1:
            board[x_][y_] = 2
        
        elif board[x_][y_] == 0:
            board[x_][y_] = 2
            rear = queue.pop()
            board[rear[0]][rear[1]] = 0
        
        elif board[x_][y_] == 2:
            isend = 1
            time += 1
            break
        
        time += 1
    
    if isend:
        break

print(time)