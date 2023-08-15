def solution(d, budget):
    
    d.sort()
    answer = len(d)
    total = sum(d)
    while total > budget:
        total -= d.pop()
        answer -= 1
    
    return answer