import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

sets = [set() for _ in range(N+1)]
classes = [[[] for _ in range(10)] for _ in range(6)]
for i in range(N):
    for j in range(5):
        classes[j+1][arr[i][j]].append(i+1)

for i in range(1, 6):
    for j in range(1, 10):
        for x in classes[i][j]:
            for y in classes[i][j]:
                if x != y:
                    sets[x].add(y)

answer = 1
Max = 0
for i in range(1, N+1):
    if len(sets[i]) > Max:
        Max = len(sets[i])
        answer = i

print(answer)