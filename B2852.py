def time_to_sec(time):
    minutes, sec = map(int, time.split(":"))
    sec += 60*minutes

    return sec

def sec_to_time(sec):
    minutes, sec = sec//60, sec%60

    return str(minutes).zfill(2) + ":" + str(sec).zfill(2)

team_one, team_two, total = 0, 0, 0
res = [0, 0]
scores = []
for _ in range(int(input())):
    team, time = map(str, input().split())
    team = int(team)
    sec = time_to_sec(time)

    scores.append([team, sec])
scores.append([0, time_to_sec("48:00")])

for score in scores:
    team, sec = score[0], score[1]

    during = sec - total
    total = sec

    if team_one > team_two:
        res[0] += during
    elif team_two > team_one:
        res[1] += during
    
    if team == 1:
        team_one += 1
    elif team == 2:
        team_two += 1

print(sec_to_time(res[0]))
print(sec_to_time(res[1]))