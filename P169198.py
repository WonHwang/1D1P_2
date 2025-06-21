def upper_cushion(sx, sy, ex, ey, m, n):
    
    if sx == ex:
        if sy < ey:
            return 0
        return (2*n-sy-ey)**2
    
    ey = n + n-ey
    
    return (sx-ex)**2 + (sy-ey)**2

def left_cushion(sx, sy, ex, ey, m, n):
    
    if sy == ey:
        if sx > ex:
            return 0
        return (sx+ex)**2
    
    ex = -ex
    
    return (sx-ex)**2 + (sy-ey)**2

def right_cushion(sx, sy, ex, ey, m, n):
    
    if sy == ey:
        if sx < ex:
            return 0
        return (2*m-sx-ex)**2
    
    ex = m + m-ex
    
    return (sx-ex)**2 + (sy-ey)**2

def under_cushion(sx, sy, ex, ey, m, n):
    
    if sx == ex:
        if sy > ey:
            return 0
        return (sy+ey)**2
    
    ey = -ey

    return (sx-ex)**2 + (sy-ey)**2

def calculate(m, n, sx, sy, ex, ey):
    
    up = upper_cushion(sx, sy, ex, ey, m, n)
    down = under_cushion(sx, sy, ex, ey, m, n)
    left = left_cushion(sx, sy, ex, ey, m, n)
    right = right_cushion(sx, sy, ex, ey, m, n)
    
    res = []
    if up:
        res.append(up)
    if down:
        res.append(down)
    if left:
        res.append(left)
    if right:
        res.append(right)
    
    res.sort()
    return res[0]

def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        ex, ey = ball[0], ball[1]
        answer.append(calculate(m, n, startX, startY, ex, ey))
    return answer