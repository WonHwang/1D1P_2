def solution(players, m, k):
    answer = 0
    servers = [0] * 24
    for i in range(24):
        if players[i] >= (servers[i]+1)*m:
            over = (players[i] - (servers[i]+1)*m) // m
            over += 1
            for j in range(i, i+k):
                if j < 24:
                    servers[j] += over
            answer += over
    return answer