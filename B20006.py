import sys
input = sys.stdin.readline

def is_in_range(first, num):
    return True if first-10 <= num <= first+10 else False

N, M = map(int, input().split())
rooms = []
for _ in range(N):
    level, name = map(str, input().rstrip().split())
    level = int(level)

    if not rooms:
        rooms.append([(level, name)])
        continue
    
    for room in rooms:
        if len(room) < M and is_in_range(room[0][0], level):
            room.append((level, name))
            break
    else:
        rooms.append([(level, name)])

for room in rooms:
    room.sort(key=lambda x:x[1])
    if len(room) < M:
        print("Waiting!")
    else:
        print("Started!")
    for i in range(len(room)):
        print(*room[i])