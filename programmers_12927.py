# 어이없는 시도
'''
def solution(n, works):
    
    total = sum(works)
    if n >= total:
        return 0
    
    total -= n
    Q, R = total // len(works), total % len(works)
    
    answer = 0
    for _ in range(R):
        answer += (Q+1)**2
    for _ in range(len(works)-R):
        answer += Q**2
    
    return answer
'''

import heapq

def solution(n, works):
    
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, -1 * work)
        
    for _ in range(n):
        Max = heapq.heappop(heap)
        
        if not Max:
            return 0
        
        Max += 1
        heapq.heappush(heap, Max)
    
    for work in heap:
        answer += work**2
    
    return answer
    
print(solution(4, [4, 3, 3])) # 12
print(solution(1, [2, 1, 2])) # 6
print(solution(3, [1, 1])) # 0