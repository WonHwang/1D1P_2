dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

direc = {
    'left': 0,
    'right': 1,
    'up': 2,
    'down': 3
}

def solution(keyinput, board):
    N, M = board[0]//2, board[1]//2
    a, b = 0, 0
    for k in keyinput:
        x, y = a + dx[direc[k]], b + dy[direc[k]]
        if  -N <= x <= N and -M <= y <= M:
            a, b = x, y
    return [a, b]
