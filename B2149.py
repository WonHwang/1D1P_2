while True:
    N = int(input())
    if not N:
        break
    N = bin(N-1)[2:][::-1]
    tmp = 1
    res = []
    for digit in N:
        if digit == "1":
            res.append(str(tmp))
        tmp *= 3
    res = ', '.join(res)
    if res:
        print("{ ", end='')
        print(res, end='')
        print(" }")
    else:
        print("{ }")