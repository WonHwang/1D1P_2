def solution(arr):
    answer = []
    start, end = -1, -1
    for i in range(len(arr)):
        if arr[i] == 2:
            if start == -1:
                start = i
                end = i
                continue
            end = i
    answer = arr[start: end+1]
    if not answer:
        answer.append(-1)
    return answer
