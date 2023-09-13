def solution(a, b, c, d):
    answer = 0
    tmp = [a, b, c, d]
    tmp.sort()
    a, b, c, d = tmp[0], tmp[1], tmp[2], tmp[3]
    if a == b and b == c and c == d:
        answer = a * 1111
    elif a == b and b == c:
        answer = (a*10 + d) ** 2
    elif b == c and c == d:
        answer = (b*10 + a) ** 2
    elif a == b and c == d:
        answer = (a + c) * abs(a - c)
    elif a == b and c != d:
        answer = c * d
    elif b == c:
        answer = a * d
    elif a != b and c == d:
        answer = a * b
    else:
        answer = a
        
    return answer
