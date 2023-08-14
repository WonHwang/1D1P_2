def solution(n):
    answer = 0
    
    result = ""
    
    while n:
        result += str(n%3)
        n //= 3
    
    tmp = 1
    for digit in result[::-1]:
        answer += int(digit) * tmp
        tmp *= 3
    
    
    return answer