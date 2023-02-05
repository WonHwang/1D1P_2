# softeer 395번 금고털이 문제

# 개인적으로 너무 엄밀하지 못한 문제라고 생각한다. 소프티어 문제는 안풀어야겠다.

from collections import deque

W, N = map(int, input().split())
jewels = []
for _ in range(N):
    jewels.append(list(map(int, input().split())))

jewels.sort(key=lambda x:x[1], reverse=True)
queue = deque(jewels)
answer = 0
while W:
    jewel = queue.popleft()
    if jewel[0] > W:
        answer += jewel[1] * W
        W = 0
        break
    answer += jewel[1] * jewel[0]
    W -= jewel[0]

print(answer)