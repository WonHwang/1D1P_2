def gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b:
        a, b = b, a%b
        
    return a

def solution(n):
    x = gcd(n, 6)
    return n*6//x//6
