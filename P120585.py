def solution(x, y):
    answer = 0
    for num in x:
        if num > y:
            answer += 1
    return answer
