def solution(s):
    stack = []
    s = list(s.split())
    for c in s:
        if c == "Z":
            stack.pop()
        else:
            stack.append(int(c))
    return sum(stack)
