import sys
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
grid = [[0, 0]] + grid + [[grid[-1][0]+1, 0]]
print(grid)
heights = set()
for i in range(1, N+1):
    heights.add(grid[i][1])
heights = list(heights)
heights.sort(reverse=True)
if heights[-1] == 0:
    heights.pop()

answer = 0
while True:
    if not heights:
        break
    
    target = heights.pop()
    i = 1
    flag = False
    while i < N+2:
        if grid[i][1] >= target:
            flag = True
        elif grid[i][1] < target:
            if flag:
                print(grid[i][0], target)
                answer += 1
                flag = False
        i += 1

print(answer)