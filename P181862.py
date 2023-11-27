def solution(myStr):
    tmp = myStr.split("a")
    tmp2 = []
    for c in tmp:
        for d in c.split("b"):
            if d:
                tmp2.append(d)
    answer = []
    for c in tmp2:
        for d in c.split("c"):
            if d:
                answer.append(d)
    if not answer:
        answer.append("EMPTY")
    return answer
