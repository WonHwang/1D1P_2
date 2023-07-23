def solution(arr):
    answer = []
    Min = min(arr)
    for ar in arr:
        if ar != Min:
            answer.append(ar)
    if not answer:
        answer.append(-1)
    return answer