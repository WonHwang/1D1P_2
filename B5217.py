for tc in range(int(input())):
    N = int(input())
    print(f"Pairs for {N}: ", end="")
    res = []
    for i in range(1, N//2+1):
        if i != N-i:
            res.append(f"{i} {N-i}")
    for i in range(len(res)-1):
        print(res[i], end = ", ")
    if res:
        print(res[-1], end="")
    print()