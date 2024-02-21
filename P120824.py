def solution(x):
    y=len(list(filter(lambda y:y%2, x)))
    return [len(x)-y,y]