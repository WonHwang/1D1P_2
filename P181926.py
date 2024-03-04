def solution(n, control):
    for c in control:
        n += {"w":1,"s":-1,"d":10,"a":-10}.get(c)
    return n