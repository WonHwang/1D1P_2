def solution(survey, choices):
    
    dic = {
        'RT': 0,
        'CF': 0,
        'JM': 0,
        'AN': 0
    }
    answer = ''
    
    for i in range(len(survey)):
        case = survey[i]
        score = choices[i]
        
        if not (case in dic):
            case = case[::-1]
            score = 8 - score
        
        score -= 4
        
        dic[case] += score
    
    for key, value in dic.items():
        if value <= 0:
            answer += key[0]
        else:
            answer += key[1]
    
    return answer