import sys
input = sys.stdin.readline

tc = 0
while True:
    tc += 1
    N = int(input())
    if not N:
        break

    names = []
    for _ in range(N):
        names.append(input().rstrip())
    
    target = {}
    for i in range(1, N+1):
        target[i] = 0
    for _ in range(2*N-1):
        num, st = map(str, input().split())
        num = int(num)
        if not target[num]:
            target[num] = 1
        else:
            target[num] = 0
    
    for i in range(1, N+1):
        if target[i]:
            print(f"{tc} {names[i-1]}")
            break