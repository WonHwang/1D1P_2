import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = dict()
for _ in range(N):
    memo[input().rstrip()] = 1
cnt = N

for _ in range(M):
    keywords = list(map(str, input().rstrip().split(',')))
    for keyword in keywords:
        if memo.get(keyword):
            memo[keyword] -= 1
            cnt -= 1
    
    print(cnt)