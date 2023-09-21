def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        if not B:
            break
        if A[i] < B[-1]:
            B.pop()
            answer += 1
    return answer
