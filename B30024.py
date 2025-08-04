import sys
from heapq import heappop, heappush
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
K = int(input())

visited = [[0 for _ in range(M)] for _ in range(N)]
heap = []
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            visited[i][j] = 1
            heappush(heap, (-grid[i][j], i, j))

for _ in range(K):
    v, a, b = heappop(heap)
    print(a+1, b+1)

    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        if 0 <= x < N and 0 <= y < M and not visited[x][y]:
            visited[x][y] = 1
            heappush(heap, (-grid[x][y], x, y))