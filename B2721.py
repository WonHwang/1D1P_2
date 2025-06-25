import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    res = 0
    for i in range(1, n+1):
        res += i*(i+1)*(i+2)//2
    print(res)