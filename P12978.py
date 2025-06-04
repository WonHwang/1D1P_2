import heapq

def solution(N, road, K):
    
    INF = 10**9

    grid = [{} for _ in range(N+1)]
    for r in road:
        a, b, d = r[0], r[1], r[2]
        grid[a][b] = min(grid[a].get(b, INF), d)
        grid[b][a] = min(grid[b].get(a, INF), d)

    for i in range(1, N+1):
        grid[i][i] = 0

    visited = [0] * (N+1)
    distance = [INF] * (N+1)
    distance[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))
    
    while heap:
        node = heapq.heappop(heap)
        distance_to_now, now = node[0], node[1]
        for node in grid[now]:
            if distance[node] > distance_to_now + grid[now][node]:
                distance[node] = distance_to_now + grid[now][node]
                heapq.heappush(heap, (distance[node], node))
    
    answer = 0
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1

    return answer