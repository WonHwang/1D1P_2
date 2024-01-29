def solution(n):
    x=n//2
    return (x+1)**2 if n%2 else 2*x*(x+1)*(2*x+1)//3