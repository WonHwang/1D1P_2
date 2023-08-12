def gcd(a, b):
    
    if b > a:
        a, b = b, a
    
    while b:
        a, b = b, a%b
    
    return a

def solution(n, m):
    
    answer = []
    d = gcd(n, m)
    answer = [d, n*m//d]
    return answer