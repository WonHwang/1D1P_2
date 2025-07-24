from collections import deque

def solution(N, number):
    answer = 0
    M = 32001
    queue = deque()
    queue.append(N)
    visited = [0] * M
    visited[N] = 1
    
    while queue:
        node = queue.popleft()
        step = visited[node]
        
        if step > 8:
            break
        
        x = int(str(N)*(step+1))
        if x < M and not visited[x]:
            visited[x] = step+1
            queue.append(x)
        
        x = node + N
        if x < M and not visited[x]:
            visited[x] = step+1
            queue.append(x)
        
        x = node - N
        if 0 <= x and not visited[x]:
            visited[x] = step+1
            queue.append(x)
        
        x = node * N
        if x < M and not visited[x]:
            visited[x] = step+1
            queue.append(x)
        
        if not node%N:
            x = node // N
            if 0 <= x < M and not visited[x]:
                visited[x] = step+1
                queue.append(x)
    
    dic = dict()
    for i in range(M):
        if visited[i]:
            dic[i] = visited[i]
    
    res = visited[::]
    for i in dic:
        for j in dic:
            
            if dic[i] + dic[j] > 8:
                continue
            
            num = i + j
            if num < M and (not visited[num] or res[num] > dic[i] + dic[j]):
                res[num] = dic[i] + dic[j]
            
            num = abs(i-j)
            if not visited[num] or res[num] > dic[i] + dic[j]:
                res[num] = dic[i] + dic[j]
            
            num = i*j
            if num < M and (not visited[num] or res[num] > dic[i] + dic[j]):
                res[num] = dic[i] + dic[j]
            
            if j and not i%j:
                num = i//j
                if not visited[num] or res[num] > dic[i] + dic[j]:
                    res[num] = dic[i] + dic[j]
                    
            if i and not j%i:
                num = j//i
                if not visited[num] or res[num] > dic[i] + dic[j]:
                    res[num] = dic[i] + dic[j]
    
    dic = dict()
    for i in range(M):
        if res[i]:
            dic[i] = res[i]
    
    result = res[::]
    for i in dic:
        for j in dic:
            
            if dic[i] + dic[j] > 8:
                continue
            
            num = i + j
            if num < M and (not res[num] or result[num] > dic[i] + dic[j]):
                result[num] = dic[i] + dic[j]
            
            num = abs(i-j)
            if not res[num] or result[num] > dic[i] + dic[j]:
                result[num] = dic[i] + dic[j]
            
            num = i*j
            if num < M and (not res[num] or result[num] > dic[i] + dic[j]):
                result[num] = dic[i] + dic[j]
            
            if j and not i%j:
                num = i//j
                if not res[num] or result[num] > dic[i] + dic[j]:
                    result[num] = dic[i] + dic[j]
                    
            if i and not j%i:
                num = j//i
                if not res[num] or result[num] > dic[i] + dic[j]:
                    result[num] = dic[i] + dic[j]
    
    return result[number] if result[number] and result[number] <= 8 else -1