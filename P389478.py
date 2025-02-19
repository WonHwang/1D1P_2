from collections import deque

def solution(n, w, num):
    warehouse = dict()
    order = 1
    for i in range(1, n+1):
        warehouse[i] = order
        if not i%w:
            continue
        if (i//w)%2:
            order -= 1
        else:
            order += 1

    answer = 0
    target = warehouse[num]
    for i in range(num, n+1):
        if warehouse[i] == target:
            answer += 1
    return answer