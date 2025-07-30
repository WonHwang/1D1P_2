for tc in range(int(input())):
    a, b = map(int, input().split())
    res = 0
    tmp = [0, 500, 300, 200, 50, 30, 10]
    A = [0]
    for i in range(1, 7):
        for j in range(i):
            A.append(tmp[i])
    if a < len(A):
        res += A[a]

    B = [0]
    for i in range(5):
        for j in range(2**i):
            B.append(2**(9-i))
    if b < len(B):
        res += B[b]
    
    print(f"{res*10000}")