def solution(board):
    answer = 0
    N, M = len(board), len(board[0])
    DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i-1][j-1]:
                DP[i][j] = min(DP[i][j-1], DP[i-1][j], DP[i-1][j-1]) + 1
                if DP[i][j] > answer:
                    answer = DP[i][j]
    return answer**2