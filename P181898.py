def solution(arr, idx):
    for i in range(len(arr)):
        if i >= idx and arr[i]:
            return i
    return -1