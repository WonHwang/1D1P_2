import sys
input = sys.stdin.readline

grid = []
for _ in range(9):
    grid.append([int(i) for i in list(input().rstrip())])

zeros = []
for i in range(9):
    for j in range(9):
        if not grid[i][j]:
            zeros.append([i, j])

def horizon(x, y):
    target = [0] * 10
    for i in range(9):
        target[grid[x][i]] += 1
    
    for i in range(1, 10):
        if target[i] > 1:
            return False
    
    return True

def vertical(x, y):
    target = [0] * 10
    for i in range(9):
        target[grid[i][y]] += 1
    
    for i in range(1, 10):
        if target[i] > 1:
            return False
    
    return True

def square(x, y):
    target = [0] * 10
    for i in range(3):
        for j in range(3):
            target[grid[3*(x//3)+i][3*(y//3)+j]] += 1
    
    for i in range(1, 10):
        if target[i] > 1:
            return False
    
    return True

answer = 0
def fill(step):
    
    global answer
    
    if answer:
        return
    
    if step == len(zeros):
        answer = 1
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end='')
            print()
        return
    
    node = zeros[step]
    x, y = node[0], node[1]
    
    for num in range(1, 10):
        grid[x][y] = num
        if horizon(x, y) and vertical(x, y) and square(x, y):
            fill(step+1)
        grid[x][y] = 0

fill(0)