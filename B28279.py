import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):

    cmd = input().rstrip()

    if cmd[0] == "1" or cmd[0] == "2":
        cmd, num = map(int, cmd.split())

        queue.appendleft(num) if cmd == 1 else queue.append(num)
    
    elif cmd[0] == "3" or cmd[0] == "4":

        if queue:
            print(queue.popleft() if cmd[0] == "3" else queue.pop())
        
        else:
            print(-1)
    
    elif cmd[0] == "5":
        print(len(queue))
    
    elif cmd[0] == "6":
        print(1 if not queue else 0)
    
    elif cmd[0] == "7" or cmd[0] == "8":
        if queue:
            print(queue[0] if cmd[0] == "7" else queue[-1])
        else:
            print(-1)