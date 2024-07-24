def solution(clothes):
    
    clothes_set = dict()
    
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_set:
            clothes_set[clothes[i][1]] += 1
        else:
            clothes_set[clothes[i][1]] = 1
    
    answer = 1
    for key in clothes_set:
        answer *= (clothes_set[key] + 1)
    answer -= 1
        
    return answer