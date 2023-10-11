def solution(score):
    answer = [0] * len(score)
    score_ = sorted(score, reverse=True, key=lambda x:x[0]+x[1])
    rank = {}
    cnt = 1
    for sc in score_:
        if rank.get(sum(sc)):
            cnt += 1
        else:
            rank[sum(sc)] = cnt
            cnt += 1
    for i in range(len(score)):
        answer[i] = rank[sum(score[i])]
    
    return answer
