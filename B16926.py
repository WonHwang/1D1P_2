import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

flatten = []

def gridtodeque(N, M, step):

    i, j = step, step
    n, m = N-step, M-step
    if i > n or j > m:
        return

    tmp = deque()
    while j < m:
        tmp.append(grid[i][j])
        j += 1
    j -= 1
    i += 1
    while i < n:
        tmp.append(grid[i][j])
        i += 1
    i -= 1
    j -= 1
    while j >= step:
        tmp.append(grid[i][j])
        j -= 1
    j += 1
    i -= 1
    while i > step:
        tmp.append(grid[i][j])
        i -= 1
    
    if tmp:
        flatten.append(tmp)

    gridtodeque(N, M, step+1)

res_grid = [[0 for _ in range(M)] for _ in range(N)]
def dequetogrid(N, M, step):

    i, j = step, step
    n, m = N-step, M-step

    if i >= n or j >= m:
        return
    
    tmp = flatten[step]
    while j < m:
        res_grid[i][j] = tmp.popleft()
        j += 1
    j -= 1
    i += 1
    while i < n:
        res_grid[i][j] = tmp.popleft()
        i += 1
    i -= 1
    j -= 1
    while j >= step:
        res_grid[i][j] = tmp.popleft()
        j -= 1
    j += 1
    i -= 1
    while i > step:
        res_grid[i][j] = tmp.popleft()
        i -= 1

    dequetogrid(N, M, step+1)

gridtodeque(N, M, 0)

for queue in flatten:
    for _ in range(R):
        queue.append(queue.popleft())

dequetogrid(N, M, 0)

for i in range(N):
    print(*res_grid[i])