from heapq import heapify, heappop, heappush

N = int(input())
mine = int(input())
heap = []
for _ in range(N-1):
    heap.append(-int(input()))
heapify(heap)

answer = 0
while heap:
    num = -heappop(heap)
    if num < mine:
        break
    num -= 1
    answer += 1
    mine += 1
    heappush(heap, -num)

print(answer)