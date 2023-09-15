def hour_to_min(time):
    
    result = 0
    h, m = map(int, time.split(":"))
    result += 60*h + m
    
    return result

def solution(book_time):
    answer = 0
    rooms = [[]]
    times = []
    for time in book_time:
        start, end = time[0], time[1]
        times.append([hour_to_min(start), hour_to_min(end)+10])
    
    times.sort(key=lambda x:(x[0], -x[1]))

    for time in times:
        for room in rooms:
            if not room:
                room.append(time[1])
                break
            
            elif room[0] <= time[0]:
                room.pop()
                room.append(time[1])
                break
        
        else:
            rooms.append([time[1]])
        
    answer = len(rooms)
    return answer
