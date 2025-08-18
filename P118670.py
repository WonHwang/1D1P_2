from collections import deque

def build_rc(left, right, center):
    answer = []
    while center:
        tmp = list(center.popleft())
        tmp = [left.popleft()] + tmp + [right.popleft()]
        answer.append(tmp)
    
    return answer

def rotate(left, right, center):
    
    center[-1].append(right.pop())
    center[0].appendleft(left.popleft())
    left.append(center[-1].popleft())
    right.appendleft(center[0].pop())

def shift_row(left, right, center):
    
    center.appendleft(center.pop())
    right.appendleft(right.pop())
    left.appendleft(left.pop())
    
def solution(rc, operations):
    left, right, center = deque(), deque(), deque()
    for row in rc:
        left.append(row[0])
        right.append(row[-1])
        center.append(deque(row[1:-1]))
    
    ops = {
        "ShiftRow": shift_row,
        "Rotate": rotate
    }
    
    for op in operations:
        ops[op](left, right, center)
    
    answer = build_rc(left, right, center)
    return answer