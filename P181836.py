def solution(picture, k):
    answer = []
    for line in picture:
        target = ""
        for digit in line:
            target += k*digit
        for _ in range(k):
            answer.append(target)
    return answer