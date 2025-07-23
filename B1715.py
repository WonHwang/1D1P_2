import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heappush(heap, int(input()))

answer = 0
while len(heap) >= 2:
    num = heappop(heap) + heappop(heap)
    answer += num
    heappush(heap, num)

print(answer)