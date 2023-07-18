# input만 20만번 가능 -> readline으로 해결
# recursion depth 조정은 필수 pypy, python 모두 필요
# recursion 값만 주면 pypy는 그냥 통과 python은 불가
# python은 recursion depth 10**5에서도 불가 10**6까지는 줘야함
# python의 한계..

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

step = 0

def dfs(con, node, visited):

    global step

    visited[node] = step
    step += 1

    for num in con[node]:
        if not visited[num]:
            dfs(con, num, visited)

N, M, R = map(int, input().rstrip().split())

visited = [0] * (N+1)

con = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    con[a].append(b)
    con[b].append(a)

for i in range(N+1):
    con[i].sort()

step += 1
dfs(con, R, visited)

for i in range(1, N+1):
    print(visited[i])