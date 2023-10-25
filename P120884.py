def solution(chicken):
    answer = 0
    while chicken:
        service = chicken // 10
        answer += service
        chicken %= 10
        chicken += service
        
        if not service:
            break
    return answer