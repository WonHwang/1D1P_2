def solution(strArr):
    answer = 0
    for s in range(1, 31):
        cnt = 0
        for w in strArr:
            if len(w) == s:
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer
