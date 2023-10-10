def solution(polynomial):
    answer = ''
    line = polynomial.split(" + ")
    x, c = 0, 0
    for d in line:
        if d[-1] == 'x':
            if d[0] == 'x':
                x += 1
            else:
                x += int(d[:-1])
        else:
            c += int(d)
    answer = ""
    if x:
        if x > 1:
            answer += f"{x}x"
        else:
            answer += "x"
    if c:
        if answer:
            answer += f" + {c}"
        else:
            answer = f"{c}"
    return answer
