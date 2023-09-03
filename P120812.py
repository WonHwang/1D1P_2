def solution(array):
    answer = 0
    arr = [0] * 1001
    for num in array:
        arr[num] += 1
    Max = max(arr)
    cnt = 0
    for i in range(1001):
        if arr[i] == Max:
            answer = i
            cnt += 1
    
    if cnt >= 2:
        answer = -1
        
    return answer