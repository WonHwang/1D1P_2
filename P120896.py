def solution(s):
    answer = ''
    for c in s:
        if s.count(c) == 1:
            answer += c
    answer = ''.join(sorted(list(answer)))
    return answer
