def solution(friends, gifts):
    answer = 0
    dic = {}
    score = {}
    answer_list = {}
    for friend in friends:
        dic[friend] = {}
        score[friend] = 0
        answer_list[friend] = 0
        for friend_ in friends:
            if friend != friend_:
                dic[friend][friend_] = 0
                
    for gift in gifts:
        give, take = map(str, gift.split())
        dic[give][take] += 1
        score[give] += 1
        score[take] -= 1
    
    for x in friends:
        for y in friends:
            if x != y:
                if dic[x][y] == dic[y][x]:
                    if score[x] == score[y]:
                        continue
                    elif score[x] > score[y]:
                        answer_list[x] += 1
                
                elif dic[x][y] > dic[y][x]:
                    answer_list[x] += 1
                    
    for friend in friends:
        if answer_list[friend] > answer:
            answer = answer_list[friend]
            
    return answer