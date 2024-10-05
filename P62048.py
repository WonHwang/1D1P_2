def get_gcd(a, b):
    res = 1
    for i in range(1, b+1):
        if not a%i and not b%i:
            res = i
    
    return res
    
def solution(w,h):
    if h > w:
        w, h = h, w
    gcd = get_gcd(w, h)
    a, b = w//gcd, h//gcd
    x = a*b - (a-1)*(b-1)
    size = h//b
    answer = w*h - x*size
    return answer