N, P = map(int, input().split())
visited = dict()
num = N
while True:
    num = num*N % P

    if visited.get(num) == 3:
        break
    visited[num] = visited.get(num, 0) + 1

answer = 0
for num in visited:
    if visited[num] >= 2:
        answer += 1
        
print(answer)