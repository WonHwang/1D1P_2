def solution(order):
    answer = 0
    for c in str(order):
        if int(c) and not int(c)%3:
            answer += 1
    return answer
