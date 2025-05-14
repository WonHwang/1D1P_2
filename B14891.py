from collections import deque

wheels = []
for i in range(4):
    wheels.append(deque(list(input())))

visited = [0] * 4

def dfs(no, direction):
    
    if no > 0:
        if not visited[no-1]:
            if wheels[no][6] != wheels[no-1][2]:
                visited[no-1] = 1
                dfs(no-1, -direction)
    
    if no < 3:
        if not visited[no+1]:
            if wheels[no][2] != wheels[no+1][6]:
                visited[no+1] = 1
                dfs(no+1, -direction)
    
    if direction == 1:
        wheels[no].appendleft(wheels[no].pop())
    
    elif direction == -1:
        wheels[no].append(wheels[no].popleft())

for _ in range(int(input())):
    visited = [0] * 4
    target, direction = map(int, input().split())
    target -= 1
    
    visited[target] = 1
    dfs(target, direction)

answer = 0
res = [1, 2, 4, 8]
for i in range(4):
    if int(wheels[i].popleft()):
        answer += res[i]

print(answer)