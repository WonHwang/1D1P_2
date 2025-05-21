# 시작 시간 순으로 정렬해야한다. 다만 끝나는 시간을 저장할때, 끝나는 시간 중 최소값이 가장 먼저 나타나야 한다. 따라서 heap을 쓰는 것이 정배가 된다.
# 따라서 (x[0], -x[1])에서 -x[1]은 크게 의미가 없다. 다만 뭔가 정렬만 가지고 queue로 처리할 수 있는 방법이 있지 않을까 고민중이다.

import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x:(x[0], -x[1]))
answer = 0
heap = []
for time in times:
    start, end = time[0], time[1]
    if heap and heap[0] <= start:
        heappop(heap)
    heappush(heap, end)
    
    size = len(heap)
    if size > answer:
        answer = size

print(answer)