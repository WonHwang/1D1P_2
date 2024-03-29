def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if not answer:
            answer.append(arr[i])
        elif arr[i] == answer[-1]:
            answer.pop()
        else:
            answer.append(arr[i])
        i += 1
    if not answer:
        answer.append(-1)
    return answer