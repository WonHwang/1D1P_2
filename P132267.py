def solution(a, b, n):
    answer = 0
    while n:
        if n < a:
            break
        tmp = (n // a) * b
        n %= a
        answer += tmp
        n += tmp
    return answer