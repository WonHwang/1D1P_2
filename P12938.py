from collections import deque

def solution(n, s):
    if n > s:
        return [-1]
    
    target = s // n
    answer = deque([target]*n)
    Sum = target*n
    while Sum < s:
        answer.appendleft(answer.pop()+1)
        Sum += 1
    
    answer = list(answer)
    answer.sort()
    return answer