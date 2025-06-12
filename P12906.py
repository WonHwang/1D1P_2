def solution(arr):
    answer = []
    last = -1
    for num in arr:
        if num == last:
            continue
        answer.append(num)
        last = num
    return answer