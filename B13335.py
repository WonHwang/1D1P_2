import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque()

time = 1
weight = 0
while trucks:
    
    if bridge and time == bridge[0][1]:
        weight -= bridge.popleft()[0]
    
    if not bridge:
        truck = trucks.popleft()
        bridge.append([truck, time+w])
        weight += truck
    
    else:
        if trucks:
            if weight + trucks[0] <= L:
                time += 1
                truck = trucks.popleft()
                bridge.append([truck, time+w])
                weight += truck
            else:
                tmp = bridge.popleft()
                weight -= tmp[0]
                time = tmp[1]
                
                if weight + trucks[0] <= L:
                    truck = trucks.popleft()
                    weight += truck
                    bridge.append([truck, time+w])

while bridge:
    time = bridge.popleft()[1]

print(time)