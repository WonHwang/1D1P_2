def istwosquare(N):
    tmp = 1
    
    while tmp <= 1024:
        if tmp == N:
            return True
        tmp *= 2
    
    return False

def solution(arr):
    while not istwosquare(len(arr)):
        arr.append(0)
    return arr