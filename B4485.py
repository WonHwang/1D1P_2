import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 10**9
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

tc = 0
while True:
    tc += 1
    N = int(input())
    if not N:
        break
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = grid[0][0]
    heap = []
    heappush(heap, (grid[0][0], [0, 0]))

    while heap:
        node = heappop(heap)
        dis_now, a, b = node[0], node[1][0], node[1][1]

        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < N and 0 <= y < N:
                tmp = dis_now + grid[x][y]
                if distance[x][y] > tmp:
                    distance[x][y] = tmp
                    heappush(heap, (tmp, [x, y]))
    
    print(f"Problem {tc}: {distance[N-1][N-1]}")