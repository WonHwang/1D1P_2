# 프로그래머스 QnA 답변용 문제

from collections import deque

s, d = map(int, input().split())
q = deque()
q.append([s, 0])
chk = [True for i in range(200001)]
chk[s] = False

while q:
    t = q.popleft()
    if t[0] == d:
        print(t[1])
        exit()

    if chk[t[0] - 1] and t[0] - 1 >= 0:
        q.append([t[0] - 1, t[1] + 1])
        chk[t[0] - 1] = False
    if chk[t[0] + 1] and t[0] + 1 <= 100000:
        q.append([t[0] + 1, t[1] + 1])
        chk[t[0] + 1] = False
    if chk[t[0] * 2] and t[0] * 2 <= 100000:
        q.append([t[0] * 2, t[1] + 1])
        chk[t[0] * 2] = False