import sys
from collections import deque
input = sys.stdin.readline

def alp_to_num(A):
    return ord(A) - ord("A")

N, M = map(int, input().split())
roots = [1] * N
conn = [[] for _ in range(N)]
disabled = [0] * N

for _ in range(M):
    A, B = map(str, input().rstrip().split())
    a, b = alp_to_num(A), alp_to_num(B)
    conn[a].append(b)
    roots[b] = 0

caught = list(input().rstrip().split())
for i in range(1, int(caught[0])+1):
    x = alp_to_num(caught[i])
    disabled[x] = 1

visited = [0] * N
answer = 0
for i in range(N):
    if roots[i] and not disabled[i]:
        queue = deque()
        visited[i] = 1
        queue.append(i)

        while queue:
            node = queue.popleft()
            
            for x in conn[node]:
                if not visited[x] and not disabled[x]:
                    visited[x] = 1
                    queue.append(x)
                    answer += 1
print(answer)