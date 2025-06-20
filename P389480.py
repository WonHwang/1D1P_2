answer = -1

def dfs(a, b, info, idx, n, m, visited):
    
    global answer
    
    if a >= n and b >= m:
        return
        
    if idx == len(info):
        if a < n and b < m:
            if answer == -1 or a < answer:
                answer = a
        return
    
    x = a + info[idx][0]
    y = b
    if not (x, y, idx+1) in visited:
        visited.add((x, y, idx+1))
        dfs(x, y, info, idx+1, n, m, visited)
    x = a
    y = b + info[idx][1]
    if not (x, y, idx+1) in visited:
        visited.add((x, y, idx+1))
        dfs(x, y, info, idx+1, n, m, visited)

def solution(info, n, m):
    
    visited = set()
    info.sort(key=lambda x:(x[0], -x[1]))
    dfs(0, 0, info, 0, n, m, visited)
    
    return answer