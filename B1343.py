def solution():
    string = input()
    c = string.split(".")
    res = []
    for s in c:
        if s:
            size = len(s)
            digit = ""
            if size%2:
                print(-1)
                return

            digit += "AAAA" * (size//4)
            digit += "B" * (size%4)
            res.append(digit)
        else:
            res.append(s)
    print(".".join(res))

solution()