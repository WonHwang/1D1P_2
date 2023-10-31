def solution(rank, attendance):
    player = []
    for i in range(len(rank)):
        if attendance[i]:
            player.append([rank[i], i])
    player.sort(key = lambda x:x[0])
    answer = player[0][1] * 10000 + player[1][1] * 100 + player[2][1]
    return answer
