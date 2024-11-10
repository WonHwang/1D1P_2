from collections import deque

string = input()
N = len(string)
idx = 0
n = 0

while idx < N:
    n += 1
    tmp = str(n)
    if string[idx] in tmp:
        queue = deque(list(tmp))
        while queue:
            if string[idx] == queue.popleft():
                idx += 1
            if idx == N:
                break

print(n)