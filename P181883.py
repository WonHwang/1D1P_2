def solution(arr, queries):
    for q in queries:
        a, b = q[0], q[1]
        
        for i in range(a, b+1):
            arr[i] += 1
    return arr