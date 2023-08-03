import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):

    string = input().rstrip()
    cmd = string[0]

    if cmd == "1":
        a, num = map(int, string.split())
        stack.append(num)
    
    elif cmd == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif cmd == "3":
        print(len(stack))
    
    elif cmd == "4":
        print(0 if stack else 1)
    
    else:
        print(stack[-1] if stack else -1)