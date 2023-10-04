def solution(quiz):
    answer = []
    ex = []
    res = []
    for q in quiz:
        tmp = q.split("=")
        ex.append(tmp[0])
        res.append(int(tmp[1]))
    for i in range(len(ex)):
        e = ex[i]
        tmp = e.split(" + ")
        if len(tmp) > 1:
            a, b = int(tmp[0]), int(tmp[1])
            if a + b == res[i]:
                answer.append("O")
            else:
                answer.append("X")
        else:
            tmp = e.split(" - ")
            a, b = int(tmp[0]), int(tmp[1])
            if a - b == res[i]:
                answer.append("O")
            else:
                answer.append("X")

    return answer