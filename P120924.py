def solution(common):
    answer = 0
    a, b, c = common[0], common[1], common[2]
    
    if 2*b == a+c:
        d = b - a
        answer = common[-1] + d
    
    elif b**2 == a*c:
        r = b // a
        answer = common[-1] * r
        
    return answer