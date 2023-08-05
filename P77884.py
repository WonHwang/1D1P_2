def get_divider_count(n):
    
    result = 0
    
    for i in range(1, n+1):
        if not n%i:
            result +=1
    
    return result

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if get_divider_count(i) % 2:
            answer -= i
        else:
            answer += i
            
    return answer