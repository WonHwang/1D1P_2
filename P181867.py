def solution(myString):
    answer = []
    cnt = 0
    for x in myString:
        if x == 'x':
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1
    answer.append(cnt)
    return answer