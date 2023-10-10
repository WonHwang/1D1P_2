# 쓰레기 문제

def get_res(a, b, c, d):
    
    if (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0]):
        return 1
    
    return 0

def solution(dots):
    
    if get_res(dots[0], dots[1], dots[2], dots[3]):
        return 1
    
    if get_res(dots[0], dots[2], dots[1], dots[3]):
        return 1
    
    if get_res(dots[0], dots[3], dots[1], dots[2]):
        return 1
    
    return 0
