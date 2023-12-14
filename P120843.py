def solution(numbers, k):
    idx = 0
    for i in range(k-1):
        idx = (idx + 2) % len(numbers)
    return idx+1
