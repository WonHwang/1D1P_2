import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int, input().split()))
switch = [0] + switch
for _ in range(int(input())):
    gen, num = map(int, input().split())
    if gen == 1:
        for i in range(num, N+1, num):
            switch[i] = 0 if switch[i] else 1
    elif gen == 2:
        for i in range(N):
            if num-i >= 1 and num+i <= N and switch[num-i] == switch[num+i]:
                continue
            else:
                switch[num] = 0 if switch[num] else 1
                for j in range(1, i):
                    switch[num-j] = 0 if switch[num-j] else 1
                    switch[num+j] = 0 if switch[num+j] else 1
                break

switch = switch[1:][::-1]
while switch:
    for i in range(20):
        if switch:
            print(switch.pop(), end=' ')
    print()