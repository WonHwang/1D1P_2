from heapq import heappop, heappush

N = int(input())
heap = []
Max = -10**10
for i in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < N:
            heappush(heap, num)
        elif len(heap) == N and num > heap[0]:
            heappop(heap)
            heappush(heap, num)
print(heappop(heap))