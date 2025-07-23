import sys
from heapq import heappop, heappush
input = sys.stdin.readline

for tc in range(int(input())):
    
    min_heap = []
    max_heap = []
    num_dict = dict()
    size = 0
    
    for _ in range(int(input())):
        op, num = map(str, input().rstrip().split())
        num = int(num)
        
        if op == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
            num_dict[num] = num_dict.get(num, 0)+1
            size += 1
        
        elif op == 'D':
            if size:
                if num == 1:
                    tmp = -heappop(max_heap)
                    num_dict[tmp] -= 1
                    if num_dict[tmp] < 0:
                        d = []
                        d.pop()
                    size -= 1
                elif num == -1:
                    tmp = heappop(min_heap)
                    num_dict[tmp] -= 1
                    if num_dict[tmp] < 0:
                        d = []
                        d.pop()
                    size -= 1
            
                if size == 1:
                    Min = heappop(min_heap)
                    if num_dict.get(Min):
                        num = Min
                        min_heap = [num]
                        max_heap = [-num]
                    else:
                        num = heappop(max_heap)
                        min_heap = [-num]
                        max_heap = [num]
                
                elif size == 0:
                    min_heap = []
                    max_heap = []
        
        print(min_heap)
        print([-i for i in max_heap])
        print(size)
        print(num_dict)
        print("------------------")
    
    print("EMPTY" if not size else f"{-heappop(max_heap)} {heappop(min_heap)}")