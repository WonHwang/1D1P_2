def solution(s):
    s = list(s)
    s.sort(key=lambda x:-ord(x))
    return ''.join(s)