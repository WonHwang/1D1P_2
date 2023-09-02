def solution(price):
    answer = 0
    if price >= 500000:
        answer = price * 8 // 10
    
    elif price >= 300000:
        answer = price * 9 // 10

    elif price >= 100000:
        answer = price * 95 // 100
    
    else:
        answer = price
    
    return answer