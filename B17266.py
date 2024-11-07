N = int(input())
M = int(input())
point = list(map(int, input().split()))
answer = 0
for i in range(M-1):
    tmp = (abs(point[i] - point[i+1]) + 1) // 2
    answer = tmp if tmp > answer else answer

answer = max(answer, point[0], N-point[-1])
print(answer)