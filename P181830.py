def solution(arr):
    n, m = len(arr), len(arr[0])
    if n > m:
        for i in range(n):
            while len(arr[i]) != n:
                arr[i].append(0)
    else:
        while len(arr) != m:
            arr.append([0]*m)
    return arr
