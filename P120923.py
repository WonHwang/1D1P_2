def solution(num, total):
    answer = []
    for i in range(-1000, 1001):
        tmp = 0
        for j in range(i, i+num):
            tmp += j
        if tmp == total:
            for j in range(i, i+num):
                answer.append(j)
            break
    return answer