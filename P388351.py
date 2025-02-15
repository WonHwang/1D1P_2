def time_to_min(time):
    h = time//100
    m = time%100
        
    return 60*h + m

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(timelogs)):
        day = startday-1
        target = time_to_min(schedules[i])
        res = True
        for j in range(len(timelogs[i])):
            day += 1
            day %= 7
            if not (day == 0 or day == 6):
                pres = time_to_min(timelogs[i][j])
                if target+10 < pres:
                    res = False
                    break
        if res:
            answer += 1
            
    return answer