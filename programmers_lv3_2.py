def solution(n, works):
    answer = 0
    total = sum(works)
    if total <= n:
        pass    
    else:
        total -= n
        rest = [(total // len(works))] * len(works)
        for i in range(total%len(works)):
            rest[i] += 1
        
        for num in rest:
            answer += num**2
    
    return answer

print(solution(4, [4, 3, 3]))