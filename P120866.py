def solution(board):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
                        board[x][y] = 2
    answer = 0
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                answer += 1
    return answer