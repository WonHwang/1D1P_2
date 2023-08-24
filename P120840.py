def solution(balls, share):
    
    pac1, pac2 = 1, 1
    answer = 1
    
    if (balls > share):
        for i in range(share+1, balls+1):
            pac1 *= i
        
        for i in range(1, balls-share+1):
            pac2 *= i
        
        answer = pac1 // pac2
    
    else:
        answer = 1
    
    return answer