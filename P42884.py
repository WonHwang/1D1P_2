def solution(routes):
    answer = 0
    N = len(routes)
    visited = [0] * N
    routes.sort(key=lambda x:x[1])
    while sum(visited) != N:
        answer += 1
        for i in range(N):
            if not visited[i]:
                point = routes[i][1]
                break
        for i in range(N):
            if not visited[i] and routes[i][0] <= point <= routes[i][1]:
                visited[i] = 1
                
    return answer