def solution(my_string, m, c):
    answer = ''
    idx = c-1
    while True:
        if idx >= len(my_string):
            break
        answer += my_string[idx]
        idx += m
    return answer
