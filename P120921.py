def solution(A, B):
    answer = 0
    while answer < len(A):
        if A == B:
            break
        A = A[-1] + A[:-1]
        answer += 1
    
    if answer == len(A):
        answer = -1
    return answer