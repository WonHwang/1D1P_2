import sys
from collections import deque
input = sys.stdin.readline

ops = ['D', 'S', 'L', 'R']

def calcaulate(op, now):
    
    if op == 'D':
        return (2*now) % 10000
    
    if op == 'S':
        return (now-1) % 10000
    
    if op == 'L':
        return (now%1000)*10 + now//1000
    
    if op == 'R':
        return (now%10)*1000 + now//10

for tc in range(int(input())):
    
    now, target = map(int, input().split())
    
    queue = deque()
    queue.append(now)
    visited = [0] * 10000
    visited[now] = "0"
    
    while queue:
        now = queue.popleft()
        step = visited[now]
        
        if now == target:
            print(step[1:])
            break
        
        for op in ops:
            res = calcaulate(op, now)
            if not visited[res]:
                visited[res] = step+op
                queue.append(res)