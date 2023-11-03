def is_possible(side):
    sides = sorted(side)
    a, b, c = sides[0], sides[1], sides[2]
    if a + b > c:
        return True
    return False

def solution(sides):
    answer = 0
    
    for i in range(1, 2001):
        sides.append(i)
        if is_possible(sides):
            answer += 1
        sides.pop()
    return answer