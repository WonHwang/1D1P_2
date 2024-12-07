from collections import deque

def solution(x, y, n):
    answer = -1
    N = 3000001
    queue = deque()
    queue.append(x)
    visited = [0] * N
    visited[x] = 1
    while queue:
        node = queue.popleft()
        step = visited[node]
        
        if node == y:
            answer = step-1
            break
        
        if node+n < N and not visited[node+n]:
            visited[node+n] = step+1
            queue.append(node+n)
        if 2*node < N and not visited[2*node]:
            visited[2*node] = step+1
            queue.append(2*node)
        if 3*node < N and not visited[3*node]:
            visited[3*node] = step+1
            queue.append(3*node)
        
    return answer