import math
def solution(box, n):
    return math.prod([x//n for x in box])