def solution(intStrs, k, s, l):
    return list(filter(lambda x:x>k, [int(x[s:s+l]) for x in intStrs]))