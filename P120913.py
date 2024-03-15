def solution(my_str, n):
    answer = []
    my_str = list(my_str[::-1])
    while my_str:
        tmp = ""
        for _ in range(n):
            if my_str:
                tmp += my_str.pop()
        answer.append(tmp)
    return answer