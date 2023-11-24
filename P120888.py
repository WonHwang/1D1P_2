def solution(my_string):
    answer = ''
    my_string = list(my_string)
    Set = set()
    for c in my_string:
        if not c in Set:
            Set.add(c)
            answer += c
    return answer
