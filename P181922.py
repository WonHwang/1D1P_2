def solution(arr, queries):
    for q in queries:
        s, e, k = q[0], q[1], q[2]
        for i in range(s, e+1):
            if not i%k:
                arr[i] += 1
    return arr